import asyncio
import json
import re
import time
from collections import Counter, defaultdict, deque
from functools import cached_property
from string import Template

import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot

from kryptone.conf import settings
from kryptone.utils.date_functions import get_current_date
from kryptone.utils.file_readers import read_document
from kryptone.utils.functions import create_filename
from kryptone.utils.iterators import keep_while
from kryptone.utils.randomizers import RANDOM_USER_AGENT
from kryptone.utils.text import clean_text, remove_punctuation, slugify

EMAIL_REGEX = r'\S+\@\S+'


def long_text_processor(tokens):
    for token in tokens:
        if len(token) <= 30:
            return True
        return False


class TextMixin:
    page_documents = []
    fitted_page_documents = []
    text_processors = [long_text_processor]

    @cached_property
    def stop_words_html(self):
        global_path = settings.GLOBAL_KRYPTONE_PATH
        filename = global_path / 'data/html_tags.txt'
        return read_document(filename, as_list=True)

    @staticmethod
    def tokenize(text):
        return text.split(' ')

    def stop_words(self, language='en'):
        global_path = settings.GLOBAL_KRYPTONE_PATH
        if language == 'en':
            file_language = 'english'
        elif language == 'fr':
            file_language = 'french'
        filename = global_path / f'data/stop_words_{file_language}.txt'
        return read_document(filename, as_list=True)

    def _common_words(self, tokens):
        counter = Counter(tokens)
        return counter.most_common()[1:5]

    def _rare_words(self, tokens):
        counter = Counter(tokens)
        return counter.most_common()[:-5:-1]

    def _remove_stop_words(self, tokens, language='en'):
        """Removes all stop words from a given document"""
        stop_words = self.stop_words(language=language)
        return list((token for token in tokens if token not in stop_words))

    def _remove_stop_words_multipass(self, tokens):
        """Remove stop words from a given document
        against both french and english language, and,
        html tags that can pollute a document"""
        english_stop_words = self.stop_words(language='en')
        french_stop_words = self.stop_words(language='fr')
        html_stop_words = self.stop_words_html

        stop_words = english_stop_words + french_stop_words + html_stop_words
        return list((token for token in tokens if token not in stop_words))

    def get_page_text(self):
        """Returns a raw extraction of 
        the document's text"""
        script = """
        return document.body.outerHTML
        """
        html = self.driver.execute_script(script)
        soup = BeautifulSoup(html, 'html.parser')
        script_tags = [tag.extract() for tag in soup.find_all('script')]
        # return self.fit(soup.text)
        return soup.text

    def run_processors(self, tokens):
        result = []
        for processor in self.text_processors:
            if not callable(processor):
                continue
            if result:
                result = list(filter(processor, result))
            else:
                result = list(filter(processor, tokens))
        return result

    def fit_transform(self, text, language='en', email_exception=False):
        text = self.fit(
            text,
            language=language,
            email_exception=email_exception
        )

        tokens = text.split(' ')
        clean_tokens = list((
            token for token in tokens
            if token not in self.stop_words(language='fr'))
        )
        text = ' '.join(clean_tokens)
        return text, clean_tokens

    def fit(self, raw_text, email_exception=False, use_multipass=False, language='en'):
        """Normalize the document by removing newlines,
        useless spaces, special characters, punctuations 
        and null values. The fit method fits the text 
        before running in depth transformation"""
        if raw_text is None:
            return None

        from nltk.tokenize import LineTokenizer, SpaceTokenizer

        tokenizer = LineTokenizer()
        tokens = tokenizer.tokenize(raw_text)

        text = ' '.join(tokens)
        no_punctuation_text = remove_punctuation(
            text, email_exception=email_exception)

        tokenizer = SpaceTokenizer()
        tokens = tokenizer.tokenize(no_punctuation_text)

        # If a text can contain both english
        # and french, use the multipass to
        # remove both fr/en stop words
        if use_multipass:
            tokens = self._remove_stop_words_multipass(tokens)
        else:
            tokens = self._remove_stop_words(tokens, language=language)

        lowered_tokens = list((token.lower() for token in tokens))
        lowered_tokens = self.run_processors(lowered_tokens)

        final_text = ' '.join(lowered_tokens).strip()
        self.fitted_page_documents.extend([final_text])
        return final_text


class SEOMixin(TextMixin):
    """A mixin for auditing a web page"""

    word_frequency_by_page = {}
    text_by_page = defaultdict(str)
    text_tokens_by_page = defaultdict(list)
    website_tokens = deque()
    stemmed_tokens = deque()
    page_audits = defaultdict(dict)
    website_word_frequency = {}

    @property
    def grouped_text(self):
        """Returns the body's text, description text
        and keyword text of an HTML document"""

    @property
    def get_page_description(self):
        script = """
        let el = document.querySelector('meta[name="description"]')
        return el && el.attributes.content.textContent
        """
        return self.driver.execute_script(script)

    @property
    def get_page_title(self):
        script = """
        let el = document.querySelector('title')
        return el && el.textContent
        """
        text = self.driver.execute_script(script)
        return self.fit(text)

    @property
    def get_page_keywords(self):
        script = """
        let el = document.querySelector('[name="keywords"]')
        return el && el.content || ''
        """
        text = self.driver.execute_script(script)
        return self.fit(self.validate_text(text))

    @cached_property
    def page_speed_script(self):
        path = settings.GLOBAL_KRYPTONE_PATH.joinpath(
            'data', 'js', 'page_speed.js'
        )
        with open(path, encoding='utf-8') as f:
            content = f.read()
        return content

    def create_word_cloud(self, frequency):
        from wordcloud import WordCloud

        page_title = self.get_page_title
        wordcloud = WordCloud()
        wordcloud.generate_from_frequencies(frequency)

        fig = pyplot.figure(figsize=[10, 10])
        pyplot.imshow(wordcloud)
        pyplot.axis('off')
        fig.savefig(f'{slugify(page_title)}')

    def create_graph(self, current_url, x_values, y_values):
        page_title = self.get_page_title
        fig = pyplot.figure()
        fig, axes = pyplot.subplots(figsize=[15, 6])
        axes.set_xlabel('Words')
        axes.set_ylabel('Count')
        axes.set_title(f"Words for {page_title}")
        axes.tick_params(which='major', width=1.00, length=5)
        # axes.text(20, 35, 'Some text')
        # axes.annotate('Something', xy=[30, 40], xytext=[14, 31], arrowprops={
        #               'facecolor': 'black', 'shrink': 0.05})
        # axes.set_xticks([0, 30, 70, 100])
        axes.legend()
        # axes.plot(x, y, 'o', label='words')
        axes.bar(x_values, y_values, color='b')
        fig.savefig(f'{slugify(page_title)}')

    def calculate_word_frequency(self, tokens):
        from nltk import FreqDist

        frequency = FreqDist(tokens)

        # Return only the values (text) for the
        # n-words which are most present in the
        # current document
        frequency_values = list(frequency.items())
        sorted_frequency = sorted(
            frequency_values,
            key=lambda x: x[1],
            reverse=True
        )[0:10]
        return frequency, sorted_frequency

    def create_stemmed_words(self, tokens):
        from nltk.stem import SnowballStemmer

        stemmer = SnowballStemmer('french')
        stemmed_words = [stemmer.stem(word=word) for word in tokens]
        self.stemmed_tokens.extendleft(stemmed_words)
        return stemmed_words

    def audit_structure(self, audit):
        """Audits the structural design of the page"""
        has_head_title = all([
            self.get_page_title is not None,
            self.get_page_title != ''
        ])
        audit['has_title'] = has_head_title

        # Check if the page has an H1 tag
        script = """
        const el = document.querySelector('h1')
        return el && el.textContent
        """
        result = self.driver.execute_script(script)
        audit['has_h1'] = False
        if result is not None:
            audit['has_h1'] = True
            audit['h1'] = clean_text(result)
        else:
            filename = create_filename(suffix='h1')

            screenshots_folder = settings.MEDIA_FOLDER / 'screenshots'
            if not screenshots_folder.exists():
                screenshots_folder.mkdir()

            path = screenshots_folder / filename
            self.driver.get_screenshot_as_file(path)

    def audit_head(self, audit):
        """Checks the head section of the
        given page"""
        page_title = self.get_page_title
        audit['title_is_valid'] = False
        if page_title is None:
            audit['title_length'] = len(page_title)
            audit['title_is_valid'] = len(page_title) <= 60

        page_description = self.get_page_description
        audit['description_is_valid'] = False
        if page_description is None:
            audit['description_length'] = len(page_description)
            audit['description_is_valid'] = len(page_description) <= 150

    def audit_images(self, audit):
        """Checks that the images of the current
        page has ALT attributes to them"""
        image_alts = []
        script = """
        return document.querySelectorAll('img')
        """
        images = self.driver.execute_script(script)
        if images:
            while images:
                try:
                    image = images.pop()
                    image_alt = self.fit(image.get_attribute('alt'))
                except:
                    pass
                else:
                    image_alts.append(image_alt)
            empty_alts = list(keep_while(lambda x: x == '', image_alts))

            unique_image_alts = set(image_alts)
            percentage_count = (len(empty_alts) / len(image_alts)) * 100
            percentage_invalid_images = round(percentage_count, 2)

            audit['pct_images_with_no_alt'] = percentage_invalid_images
            audit['image_alts'] = list(unique_image_alts)
            return percentage_invalid_images, unique_image_alts
        else:
            audit['pct_images_with_no_alt'] = 0
            audit['image_alts'] = []
            return 0, set()

    def audit_structured_data(self, audit):
        """
        Checks if the website has structured data

        >>> self.audit_structured_data({})
        ... True, {}
        """
        has_structured_data = False
        structured_data_type = None
        script = """
        let el = document.querySelector('script[type*="ld+json"]')
        return el && el.textContent
        """
        content = self.driver.execute_script(script)
        if content:
            content = json.loads(content)
            has_structured_data = True
            # Try to get @type otherwise just return the content
            structured_data_type = content.get('@type', None) or content

        audit['has_structured_data'] = has_structured_data
        audit['structured_data_type'] = structured_data_type
        return has_structured_data, structured_data_type

    def audit_page_speed(self, audit):
        result = self.driver.execute_script(self.page_speed_script)
        audit['timing'] = result

    def audit_page_status_code(self, current_url, audit):
        async def sender():
            headers = {'User-Agent': RANDOM_USER_AGENT()}
            try:
                response = requests.get(str(current_url), headers=headers)
            except:
                # If we get an error when trying to send
                # the request, just put status code 0
                audit['status_code'] = 0
            else:
                audit['status_code'] = response.status_code

        async def main():
            await sender()

        asyncio.run(main())

    def audit_page(self, current_url, generate_graph=False):
        raw_text = self.get_page_text()
        text, tokens = self.fit_transform(raw_text)
        self.website_tokens.extendleft(tokens)

        self.text_by_page[str(current_url)] = text
        self.text_tokens_by_page[str(current_url)] = tokens

        frequency, sorted_frequencies = self.calculate_word_frequency(tokens)
        self.word_frequency_by_page[str(current_url)] = dict(frequency)
        self.website_word_frequency.update(dict(frequency))

        if generate_graph:
            x_values = [x[0] for x in sorted_frequencies]
            y_values = [x[1] for x in sorted_frequencies]
            self.create_graph(current_url, x_values, y_values)

        audit = {
            'date': get_current_date(),
            'title': self.get_page_title,
            'description': self.get_page_description,
            'url': str(current_url),
            'page_content_length': len(self.get_page_text()),
            'is_https': current_url.is_secured,
        }

        self.audit_structure(audit)
        # self.audit_head(audit)
        # self.audit_structured_data(audit)
        # self.audit_images(audit)
        # self.audit_page_speed(audit)
        self.audit_page_status_code(current_url, audit)

        self.page_audits[str(current_url)] = audit
        return audit


class EmailMixin(TextMixin):
    emails_container = set()

    @staticmethod
    def identify_email(value):
        """Checks if the value could be
        an email address"""
        # Skip social media handles
        if value.startswith('@'):
            return None

        if '@' in value:
            return value

        return None

    @staticmethod
    def parse_url(element):
        value = element.get_attribute('href')
        if value is not None and '@' in value:
            return value
        return None

    def parse_protected_email(self, email):
        pass

    def emails(self, text, elements=None):
        """Returns a set of valid email
        addresses on the current page"""
        def validate_values(value):
            if value is None:
                return False

            result = re.match(EMAIL_REGEX, value)
            if result:
                return True

        emails_from_text = self.find_emails_from_links(elements)
        emails_from_links = self.find_emails_from_text(text)
        unvalidated_emails = emails_from_text.union(emails_from_links)

        valid_items = list(filter(validate_values, unvalidated_emails))
        self.emails_container = self.emails_container.union(valid_items)

    def find_emails_from_text(self):
        """Return emails embedded in plain text"""
        text = self.fit_transform(self.get_page_text(), email_exception=True)
        emails_from_text = map(
            self.identify_email,
            text.split(' ')
        )
        return set(emails_from_text)

    def find_emails_from_links(self, elements):
        """Return emails present in links"""
        emails_from_urls = map(self.parse_url, elements)
        return set(emails_from_urls)


class ScrollMixin:
    """A mixin that implements special scrolling
    functionnalities to the spider"""

    def scroll_window(self, wait_time=5, increment=1000, stop_at=None):
        """Scrolls the entire window by incremeting the current
        scroll position by a given number of pixels"""
        can_scroll = True
        new_scroll_pixels = 1000

        while can_scroll:
            scroll_script = f"""window.scroll(0, {new_scroll_pixels})"""

            self.driver.execute_script(scroll_script)
            # Scrolls until we get a result that determines that we
            # have actually scrolled to the bottom of the page
            has_reached_bottom = self.driver.execute_script(
                """return (window.innerHeight + window.scrollY) >= (document.documentElement.scrollHeight - 100)"""
            )
            if has_reached_bottom:
                can_scroll = False

            current_position = self.driver.execute_script(
                """return window.scrollY"""
            )
            if stop_at is not None and current_position > stop_at:
                can_scroll = False

            new_scroll_pixels = new_scroll_pixels + increment
            time.sleep(wait_time)

    def scroll_page_section(self, xpath=None, css_selector=None):
        """Scrolls a specific portion on the page"""
        if css_selector:
            selector = """const mainWrapper = document.querySelector('{condition}')"""
            selector = selector.format(condition=css_selector)
        else:
            # selector = self.evaluate_xpath(xpath)
            # selector = """const element = document.evaluate("{condition}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)"""
            # selector = selector.format(condition=xpath)
            pass

        body = """
        const elementToScroll = mainWrapper.querySelector('div[tabindex="-1"]')

        const elementHeight = elementToScroll.scrollHeight
        let currentPosition = elementToScroll.scrollTop

        // Indicates the scrolling speed
        const scrollStep = Math.ceil(elementHeight / {scroll_step})

        currentPosition += scrollStep
        elementToScroll.scroll(0, currentPosition)

        return [ currentPosition, elementHeight ]
        """.format(scroll_step=self.default_scroll_step)

        script = css_selector + '\n' + body
        return script

    def scroll_into_view(self, css_selector):
        """Scrolls directly into an element of the page"""
        script = """
        const el = document.querySelector('$css_selector')
        el.scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' })
        """
        template = Template(script)
        script = template.substitute(**{'css_selector': css_selector})
        self.driver.execute_script(script)

# class TestClass(TextMixin):
#     def __init__(self):
#         self.driver = None

#     def start(self):
#         self.driver = get_selenium_browser_instance(browser_name='Edge')
#         self.driver.get('https://www.noiise.com/agences/lille/')
#         print(self.fit_transform())
#         time.sleep(10)


# c = TestClass()
# # c.start()

# response = requests.get('https://www.noiise.com/agences/lille/')
# s = BeautifulSoup(response.content, 'html.parser')
# r = [tag.extract() for tag in s.find_all('script')]
# m = TextMixin()
# text, tokens = m.fit_transform(text=s.text)
# print(text)
