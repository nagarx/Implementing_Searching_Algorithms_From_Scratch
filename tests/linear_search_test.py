import unittest
from src.Search_Algorithms.linear_search import linear_search
class TestLinearSearch(unittest.TestCase):

    def test_element_found(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = linear_search(arr, 25)
        self.assertEqual(result, 2)

    def test_element_not_found(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = linear_search(arr, 100)
        self.assertEqual(result, -1)

    def test_duplicates(self):
        arr = [1, 2, 3, 3, 5]
        result = linear_search(arr, 3)
        self.assertTrue(result in [2, 3])

    def test_empty_array(self):
        arr = []
        result = linear_search(arr, 3)
        self.assertEqual(result, -1)


# Run the test suite
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLinearSearch))