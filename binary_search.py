#!/home/styxny/algs/bin/python
"""
An easy implementation of binary search

Author: Styxny
"""

import numpy as np

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1

        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    my_list = [1,2,3,5,9]

    print(binary_search(my_list, 9))