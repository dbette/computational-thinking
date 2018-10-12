def quicksort(input_array):
    """
    Implementation of the quicksort algorithm.
    
    Args:
        input_array: list consisting of integers.
    Return:
        sorted list.
    """
    
    left = []
    right = []
    pivot = []
    
    if len(input_array) <= 1:
        return input_array
    else:
        pivot_number = input_array[-1]
        for item in input_array:
            if item < pivot_number:
                left.append(item)
            elif item == pivot_number:
                pivot.append(item)
            else:
                right.append(item)

        left = quicksort(left)
        right = quicksort(right)
        
        return left + pivot + right