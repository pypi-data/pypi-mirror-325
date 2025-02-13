import unittest

from kryptone.utils.text import clean_dictionnary, remove_accents, remove_punctuation


class TestText(unittest.TestCase):
    def test_dictionnary(self):
        data = {'name': 'Kendall '}
        clean_data = clean_dictionnary(data)
        self.assertDictEqual(clean_data, {'name': 'Kendall'})

    def test_list(self):
        data = [{'name': 'Kendall '}]
        clean_data = clean_dictionnary(data)
        self.assertListEqual(clean_data, [{'name': 'Kendall'}])


class TestTextCleaning(unittest.TestCase):
    def test_remove_accents(self):
        text = remove_accents('chloé')
        self.assertEqual(text, 'chloe')

    def test_remove_punctuaction(self):
        text = remove_punctuation('kendall, jenner')
        self.assertEqual(text, 'kendall jenner')

        text = remove_punctuation('kendall_jenner', keep=['_'])
        self.assertEqual(text, 'kendall_jenner')


if __name__ == '__main__':
    unittest.main()
