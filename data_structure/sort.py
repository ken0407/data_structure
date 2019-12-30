# -*- coding: utf-8 -*-
#from . import helpers

def bubble_sort(x:list)->list:
    """this is bubble sort algorithm."""
    flag = True
    while flag:
        flag = False
        for i in range(len(x)-1):
            if x[i]>x[i+1]:
                tmp = x[i]
                x[i] = x[i+1]
                x[i+1] = tmp
                flag = True
    return x

def choose_sort(x:list)->list:
    """this is choose sort algorithm."""
    for i in range(len(x)):
        min = x[i]
        min_idx = i
        for j in range(i, len(x)):
            if x[j] < min:
                min = x[j]
                min_idx = j
        x[min_idx] = x[i]
        x[i] = min

    return x

def merge_sort(x:list)->list:
    def merge(left, right):
        i = 0
        j = 0
        return_list = []
        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                return_list.append(left[i])
                i += 1
            else:
                return_list.append(right[j])
                j += 1
        if i == len(left)-1:
            return_list.extend(right[j:])
        if j == len(right)-1:
            return_list.extend(left[i:])

        return return_list
    if len(x) <= 1:
        return x

    center = len(x) // 2
    x_a = x[:center]
    x_b = x[center:]
    x_a = merge_sort(x_a)
    x_b = merge_sort(x_b)

    return merge(x_a, x_b)