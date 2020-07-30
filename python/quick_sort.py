#!/home/styxny/algs/bin/python
"""
Implementation of quicksort algorithm

Author: Styxny
"""

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    print(quicksort([10,13,4,8,2,11,7,5]))