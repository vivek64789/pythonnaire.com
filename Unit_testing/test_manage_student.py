import unittest
from Frontend.manage_student import ManageStudent


class TestManageStudent(unittest.TestCase):

    def setUp(self):
        self.unsorted_list = ['Dean', 'Emely', 'Vivek', 'Tobias', 'Sofia', 'Porter', 'Cloe', 'Alana', 'Misty']
        self.sorted_list = ['Alana', 'Cloe', 'Dean', 'Emely', 'Misty', 'Porter', 'Sofia', 'Tobias', 'Vivek']
        self.sorted_reversed_list = [65, 43, 23, 14, 5, 3, 1]
        self.same_list = [1, 1, 1, 1, 1, 1, 1]
        self.empty_list = []
        self.single_list = [7]
        self.repeated_list = [2, 2, 5, 4, 33, 3, 333, 4, 4, 8, 8]
        self.negative_list = [-5, -9, -4, -3, -4, -1]
        self.negative_sorted_list = [-9,-5,-4,-4,-3,-1]
        self.obj = ManageStudent

    def test_bubble_sort_already_sorted(self):
        expected = self.sorted_list
        actual = self.obj.bubble_sort(self.sorted_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_unsorted(self):
        expected = self.sorted_list
        actual = self.obj.bubble_sort(self.unsorted_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_reversed(self):
        expected = [1, 3, 5, 14, 23, 43, 65]
        actual = self.obj.bubble_sort(self.sorted_reversed_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_same(self):
        expected = self.same_list
        actual = self.obj.bubble_sort(self.same_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_empty(self):
        expected = self.empty_list
        actual = self.obj.bubble_sort(self.empty_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_single(self):
        expected = self.single_list
        actual = self.obj.bubble_sort(self.single_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_repeated(self):
        expected = [2, 2, 3, 4, 4, 4, 5, 8, 8, 33, 333]
        actual = self.obj.bubble_sort(self.repeated_list)
        self.assertEqual(expected, actual)

    def test_bubble_sort_negative(self):
        expected = [-9, -5, -4, -4, -3, -1]
        actual = self.obj.bubble_sort(self.negative_list)
        self.assertEqual(expected, actual)

    def test_binary_search_empty(self):
        actual = self.obj.binary_search(self.empty_list, '')
        self.assertIsNone(actual)

    def test_binary_search_sorted(self):
        expected = 'anand'
        actual = self.obj.binary_search(self.sorted_list, 'anand')
        self.assertNotEqual(expected, actual)

    def test_binary_search_sorted_found(self):
        expected = 'Dean'
        actual = self.obj.binary_search(self.sorted_list, 'Dean')
        self.assertEqual(expected, actual)

    def test_binary_search_unsorted_notFound(self):
        expected = None
        actual = self.obj.binary_search(self.unsorted_list, 'Vivek')
        self.assertEqual(expected, actual)

    def test_binary_search_sorted_atMidFound(self):
        expected = 'Misty'
        actual = self.obj.binary_search(self.sorted_list, 'Misty')
        self.assertEqual(expected, actual)

    def test_binary_search_sorted_notFound(self):
        actual = self.obj.binary_search(self.sorted_list, 'Found?')
        self.assertIsNone(actual)

    def test_binary_search_negative_sorted_found(self):
        expected = -9
        actual = self.obj.binary_search(self.negative_sorted_list, -9)
        self.assertEqual(expected, actual)
