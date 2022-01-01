def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        for index in range(len(array)):
            if array[index] < pivot:
                less.append(array[index])

        greater = []
        for index in range(len(array)):
            if array[index] > pivot:
                greater.append(array[index])

        return quicksort(less) + [pivot] + quicksort(greater)


arr = [10, 5, 2, 3, 6, 54, 7, 326, 6,9]

print(quicksort(arr))
