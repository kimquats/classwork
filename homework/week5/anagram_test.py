import unittest
from anagram import *

class TestAnagram(unittest.TestCase):

    def test_normalize(self):
        res = normalize('bar')
        self.assertEqual(res, 'abr')
        res = normalize('')
        self.assertEqual(res, '')
        res = normalize("dude,")
        self.assertEqual(res, 'ddeu')
        res = normalize("This sentence contains 4 e's.")
        self.assertEqual(res, 'acceeeehiinnnnossssttt')
        res = normalize('128;,.')
        self.assertEqual(res, '')

    def test_remove_letters(self):
        res = remove_letters('', 'a')
        self.assertEqual(res, 'a')
        res = remove_letters('', '')
        self.assertEqual(res, '')
        res = remove_letters('a', '')
        self.assertEqual(res, None)
        res = remove_letters('abc', 'abcdefg')
        self.assertEqual(res, 'defg')

    def test_anagrams(self):
        res = anagrams('', [])
        self.assertEqual(res, [])
        res = anagrams('foobar', ['foo', 'bar'])
        self.assertEqual(res, ['foo bar', 'bar foo'])
        res = anagrams('', ['foo', 'bar'])
        self.assertEqual(res, [])

if __name__ == '__main__':
    unittest.main()
