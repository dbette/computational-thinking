unsorted_list = [7, 5, 3, 2, 6, 8, 9, 1, 8]

def split(input_array):
    if len(input_array) < 2:
        return input_array
 
    split_point = len(input_array)//2
    left_list = split(input_array[:split_point]) 
    right_list = split(input_array[split_point:])

split(unsorted_list)
    


def merge(left, right):

    sorted_list = []
    left_index = 0
    right_index = 0

    while len(sorted_list) < (len(left) + len(right)): 

        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

        if len(left)==left_index:
            sorted_list.extend(right[right_index:])
            break # more efficient, because if clause doesn't need to be evaluated
            
        if len(right)==right_index:
            sorted_list.extend(left[left_index:])

    print(sorted_list)

merge([1,3,4,7], [2,6,8,])


                