def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list [0] > sub_max else sub_max


num_list = [2,4,6]
max(num_list)