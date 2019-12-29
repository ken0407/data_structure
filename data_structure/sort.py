# -*- coding: utf-8 -*-
#from . import helpers

def insert_sort(x:list)->list:
    """this is quick sort algorithm."""
    for i in range(len(x)):
        min = x[i]
        min_idx = i
        for j in range(i, len(x)):
            if x[j] < min:
                min = x[j]
                min_idx = j
        x[min_idx] = x[i]
        x[i] = min
    print(x)
    return x

if __name__=='__main__':
    x = [4, 6, -12, 200, -1432, 0]
    x = insert_sort(x)
    print(x)