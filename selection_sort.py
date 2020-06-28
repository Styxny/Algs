#!/home/styxny/algs/bin/python
"""
A simple implementation of selection sort

Author: Styxny
"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == '__main__':
    print(selectionSort([3,8,4,11,6,9]))