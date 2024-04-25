#!/usr/bin/python3
""" Script to find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    def binary_search(arr, low, high):
        """ Helper function to perform binary search for a peak element """
        if low == high:
            return arr[low]

        mid = (low + high) // 2
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
                (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid])):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search(arr, low, mid - 1)
        else:
            return binary_search(arr, mid + 1, high)

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
