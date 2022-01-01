# This is how to implement a selection sort in python

def find_smallest(arr):
    smallest_number = arr[0]  # we assume the smallest number to be the first number
    smallest_index = 0  # the index of the smallest number is 0 since arrays start there
    for index in range(len(arr)):  # loop through the array
        if arr[index] < smallest_number:  # compare each number with the smallest number
            smallest_number = arr[index]  # if item < smallest number, item will be the smallest number
            smallest_index = index  # smallest index will be the index
    return smallest_index  # return the smallest index


def selection_sort(arr):
    sorted_array = []  # created new sorted empty array
    for index in range(len(arr)):  # loop through the array
        smallest = find_smallest(arr)  # get the smallest number in the list
        sorted_array.append(arr.pop(smallest))  # see explanation below
    return sorted_array  # return sorted array


unsortedArr = [1, 5, 3, 6, 2, 10]
print(selection_sort(unsortedArr))
'''
Since the .pop() returns the number that was removed, we are basically adding the smallest number that was taken out 
of the original array and appending it to the sorted array
'''
