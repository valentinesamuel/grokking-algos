def merge_sort(array):
      if len(array) < 2:
          return array
      
      midpoint=len(array)//2
      left=merge_sort(array[:midpoint])
      right=merge_sort(array[midpoint:])
      return merge(left, right)

def merge(left, right):
      result=[]
      left_index = 0
      right_index = 0
      while left_index < len(left) and right_index < len(right):
          if left[left_index] < right[right_index]:
              result.append(left[left_index])
              left_index += 1
          else:
              result.append(right[right_index])
              right_index += 1
      result += left[left_index:]
      result += right[right_index:]
      return result



arr = [10, 5, 2, 3, 6, 54, 7, 326, 6,9]
sorted_array = merge_sort(arr)
print(arr)
print(sorted_array)