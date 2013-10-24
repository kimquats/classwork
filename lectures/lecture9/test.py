import unittest
import binarysearch

class TestSearch(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1, binarysearch.search([0,1,2], 1))

    def test_one_element_in_list(self):
        self.assertEqual(0, binarysearch.search([1], 0))

    def element_not_in_list(self):
        self.assertEqual(None, binarysearch.search([1, 2, 3], 3))

    def element_in_list_of_many(self):
        self.assertEqual(1, binarysearch.search([1, 2, 3, 4], 1))

if __name__ == '__main__':
    unittest.main()

# domain of lst =  empty list, list containing one element, 
# domain of elt = first element, last element, even numbered element, odd-numbered element, 
# center element
