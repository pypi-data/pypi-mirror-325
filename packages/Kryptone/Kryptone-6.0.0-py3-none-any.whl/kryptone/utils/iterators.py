import datetime
import itertools
import re
from collections import OrderedDict, defaultdict
from functools import cached_property
from string import Template
from urllib.parse import urlencode, urlparse

import pytz


def drop_null(items, remove_empty_strings=True):
    for item in items:
        if remove_empty_strings and item == '':
            continue

        if item is not None:
            yield item


def keep_while(predicate, items):
    for item in items:
        if not predicate(item):
            continue
        yield item


def drop_while(predicate, items):
    for item in items:
        if predicate(item):
            continue
        yield item


def group_by(predicate, items):
    lhvs = []
    rhvs = []
    for item in items:
        if predicate(item):
            lhvs.append(item)
        else:
            rhvs.append(item)
    return lhvs, rhvs


def iterate_chunks(items, n):
    """Function that creates and iterates over
    chunks of data

    >>> iterate_chunks([1, 2, 3], 2)
    ... [1, 2]
    ... [3]
    """
    if n < 1:
        raise ValueError(f'n must be greater or equal to 1. Got: {n}')

    it = iter(items)
    while True:
        chunked_items = itertools.islice(it, n)
        try:
            first_element = next(chunked_items)
        except StopIteration:
            return
        yield itertools.chain((first_element,), chunked_items)


class CombinedIterators:
    def __init__(self, *iterators):
        self.iterators = list(iterators)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name} {self.iterators}>'

    def __iter__(self):
        for url in self.urls:
            yield url[0]

    def __add__(self, obj):
        # Add the new iterator to the
        # list of iterators
        self.iterators.append(obj)
        return self

    @cached_property
    def urls(self):
        urls_list = []
        for item in self.iterators:
            urls = list(item)
            for url in urls:
                urls_list.append(url)
        return urls_list

    @cached_property
    def classified_images(self):
        return_result = []
        for item in self.iterators:
            return_result.append(item.classified_images)
        return return_result

    @cached_property
    def as_dict(self):
        return_result = {}
        for item in self.iterators:
            return_result.update(item.as_dict)
        return return_result

    @cached_property
    def as_csv(self):
        items = []
        for item in self.iterators:
            urls = list(item)
            for alt, url in urls:
                items.append([item.page_url, alt, url])
        return items


class PageImagesIterator:
    """An iterator for storing images collected
    on a given page. This will by default get any
    images on the page except base64 types

    Subclass PageImagesIterator to collect specific
    types of images
    """

    images_list_filter = []

    def __init__(self, current_url, image_elements):
        self.urls = []
        self.page_url = current_url
        self._cached_images = []
        self.extensions = set()

        from kryptone.utils.urls import URL
        for image in image_elements:
            image_alt = image.get_attribute('alt')
            src = image.get_attribute('src')

            instance = URL(src)
            if instance.is_empty:
                continue

            if instance.is_image:
                if instance.get_extension not in self.images_list_filter:
                    continue
                self.extensions.add(instance.get_extension)

                if src.startswith('data:image'):
                    continue
                self.urls.append([image_alt, instance.raw_url])

    def __repr__(self):
        return f'<PageImages: {self.page_url}, {len(self.urls)} images>'

    def __iter__(self):
        for url in self.urls:
            yield url[0]

    def __len__(self):
        return len(self.urls)

    def __add__(self, obj):
        return CombinedIterators(self, obj)

    @cached_property
    def urls(self):
        items = []
        for url in self.urls:
            items.append(url[1])
        return items

    @cached_property
    def classified_images(self):
        classified_images_container = defaultdict(set)
        for extension in self.extensions:
            container = classified_images_container[extension]
            for url in self.urls:
                container.add(url[1])
        return classified_images_container

    @cached_property
    def as_dict(self):
        """Returns each collected under a dict format
        useful for saving the data in a JSON file"""
        def normalize_data(values):
            name = values[0]
            name = None if name == '' else name
            return {
                'name': name,
                'url': values[1]
            }
        return {self.page_url: list(map(normalize_data, self.urls))}

    @cached_property
    def as_csv(self):
        items = []
        for alt, url in self.urls:
            items.append([self.page_url, alt, url])
        return items


class JPEGImagesIterator(PageImagesIterator):
    """Will collect only jpg and jpeg images"""

    images_list_filter = ['jpg', 'jpeg']


class EcommercePageImagesIterator(JPEGImagesIterator):
    """Same as PageImagesIterator but applies an additional
    filter to classify images related by a specific
    collection together
    """


class AsyncIterator:
    def __init__(self, data, by=10):
        self.data = data
        self.by = by

    def __alen__(self):
        return len(self.data)

    def __aiter__(self):
        result = iterate_chunks(self.data, self.by)
        for item in result:
            yield list(item)
