import unittest

from SortingAlgo import bubble_sort, selection_sort

class TestSorting(unittest.TestCase):
    def test_basic_bubble_sort_works(self):
        self.assertEqual(bubble_sort([4, 2, 6, 6, 5]), [2, 4, 5, 6, 6])
    def test_basic_bubble_sort_fails(self):
        self.assertNotEqual(bubble_sort([4, 2, 6, 6, 5]), [2, 5, 4, 6, 6])    
    def test_basic_selection_sort_works(self):
        self.assertEqual(selection_sort([4, 2, 6, 6, 5]), [2, 4, 5, 6, 6])
    def test_basic_selection_sort_fails(self):
        self.assertNotEqual(selection_sort([4, 2, 6, 6, 5]), [2, 5, 4, 6, 6])
    def test_basic_bubble_sort_string(self):
        self.assertEqual(bubble_sort(['cat', 'bat', 'fat', 'ant', 'rant']), ['ant', 'bat', 'cat', 'fat', 'rant'])
    def test_basic_bubble_sort_mix(self):
        self.assertEqual(bubble_sort([4, 2, 'Fun', 'Ben', 5]), [2, 4, 5, 'Ben', 'Fun'])    
    def test_basic_selection_sort_string(self):
        self.assertEqual(selection_sort(['cat', 'bat', 'fat', 'ant', 'rant']), ['ant', 'bat', 'cat', 'fat', 'rant'])
    def test_basic_selection_sort_mix(self):
        self.assertEqual(selection_sort([4, 2, 'Fun', 'Ben', 5]), [2, 4, 5, 'Ben', 'Fun'])
    
    
if __name__ == '__main__':
    unittest.main()