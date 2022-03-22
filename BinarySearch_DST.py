from timer import time_it

@time_it
def linear_search(numbers_list, target_number):
    for x in range(len(numbers_list)):
        if numbers_list[x] == target_number:
            return x
    return -1

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)






@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

@time_it
def binary_search_recursive(numbers_list, target_number, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, target_number, left_index, right_index)



if __name__ == '__main__':
    numbers_list = [1,4,4,4,11,15,16,15,17,21,34,34,56]
    number_to_find = 4

    #count = linear_search(numbers_list, number_to_find)
    #print("Count of LS is " + str(count+1))

    #count = binary_search(numbers_list, number_to_find)
    #print("Number found at " + str(count) + " using BS")



