# PFDS Exercise 7
# Author: Anuroop Bisaria
# Linear and Binary Search

def lin_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def bin_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_search(arr, l, mid-1, x)
        else:
            return bin_search(arr, mid + 1, r, x)
    else:
        return -1
