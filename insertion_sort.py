unsorted_list = [5, 8, 4, 6, 3, 9, 1, 2, 7]

for j in range(1, len(unsorted_list)):
    key = unsorted_list[j]
    i = j-1
    while i>=0 and unsorted_list[i]>key:
        unsorted_list[i+1] = unsorted_list[i]
        i -= 1
    unsorted_list[i+1]=key
    print(unsorted_list)