import unittest
from .context import data_structure

class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        x =[4, 6, -12, 200, -1432, 0]
        x = data_structure.bubble_sort(x)
        for i in range(len(x) - 1):
            assert x[i + 1] > x[i], 'bubble sort is wrong.'

    def test_choose_sort(self):
        x = [4, 6, -12, 200, -1432, 0]
        x = data_structure.choose_sort(x)
        for i in range(len(x)-1):
            assert x[i+1] > x[i], 'choose sort is wrong.'

    def test_merge_sort(self):
        x = [4, 6, -12, 200, -1432, 0]
        x = data_structure.merge_sort(x)
        for i in range(len(x) - 1):
            assert x[i + 1] > x[i], 'merge sort is wrong.'
