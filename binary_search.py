# This is how to implement a binary search in python

def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1 # high is the len of the list -1, because of the index

    while low <= high: # so long as the higher end is greater than the lower end
        middle_element = (low + high) # the middle element is the beginning of the list plus end
        guess = sorted_list[middle_element] # our guess is the middle of the list
        if guess == item: # when we find the item,
            return middle_element # we return the index
        if guess > item: # if our guess is bigger than the item
            high = middle_element - 1 # reset the high to the middle
        else:
            low = middle_element + 1 # if not, let the beginning be middle
    return None


my_list = [1, 3, 5, 7, 9, 10, 12]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
