mylst = [3, 4, 1, 7, 9, 10, 3, 6]
def merge(list_a, list_b):
    list_c = []
    while list_a != [] and list_b != []:
        if list_a[0] < list_b[0]:
            list_c.append(list_a.pop(0))
        else:
            list_c.append(list_b.pop(0))

    if list_a == []:
        list_c += list_b
    else:
        list_c += list_a
    return list_c

def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    else:
        middle = len(unsorted)//2
        # Call its own function here: merge_sort()
        left = merge_sort(unsorted[:middle])
        right = merge_sort(unsorted[middle:])
        return merge(left, right)


x = merge_sort(mylst)
print('Before merge sort:', mylst)
print('After merge sort:', x)
