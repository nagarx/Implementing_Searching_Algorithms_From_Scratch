import unittest
from src.Search_Algorithms.ubiquitous_binary_search import ubiquitous_binary_search  # Adjust the import based on your directory structure

class TestUbiquitousBinarySearch(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(ubiquitous_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 4)
        self.assertEqual(ubiquitous_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), -1)
        self.assertEqual(ubiquitous_binary_search([], 5), -1)
        self.assertEqual(ubiquitous_binary_search([5], 5), 0)
        self.assertEqual(ubiquitous_binary_search([5], 4), -1)

    def test_advanced_cases(self):
        self.assertEqual(ubiquitous_binary_search(list(range(1, 10**6 + 1)), 999_999), 999_998)
        self.assertEqual(ubiquitous_binary_search([1, 2, 2, 3, 4, 4, 5], 4), 4)
        self.assertEqual(ubiquitous_binary_search([0.1, 0.2, 0.3, 0.4, 0.5], 0.4), 3)

if __name__ == '__main__':
    unittest.main()
