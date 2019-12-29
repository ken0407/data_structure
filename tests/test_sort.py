import unittest
from .context import data_structure

class TestSort(unittest.TestCase):
    def test_insert_sort(self):
        x = [4, 6, -12, 200, -1432, 0]
        x = data_structure.insert_sort(x)
        for i in range(len(x)-1):
            assert x[i+1] > x[i], 'insert sort is wrong.'
