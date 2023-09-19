import unittest
from src.Search_Algorithms.binary_search import binary_search
class TestBinarySearch(unittest.TestCase):

    def test_element_found(self):
        arr = [11, 12, 22, 25, 34, 64, 90]
        result = binary_search(arr, 25)
        self.assertEqual(result, 3)

    def test_element_not_found(self):
        arr = [11, 12, 22, 25, 34, 64, 90]
        result = binary_search(arr, 100)
        self.assertEqual(result, -1)

    def test_duplicates(self):
        arr = [1, 2, 3, 3, 5]
        result = binary_search(arr, 3)
        self.assertTrue(result in [2, 3])

    def test_empty_array(self):
        arr = []
        result = binary_search(arr, 3)
        self.assertEqual(result, -1)


# Run the test suite
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestBinarySearch))