def bi_search(sorted_list, value):
# left to 0
    left = 0

# right to highest index in list
    right = len(sorted_list) - 1

# loop that ends when left > right
    while left <= right:

# mid to int between left and right
        mid = int((left + right)/2)

# if sorted_list[mid] > value  set right to mid
        if sorted_list[mid] > value:
            right = mid - 1
# if sorted_list[mid] < value  set left to mid
        elif sorted_list[mid] < value:
            left = mid + 1
# if sorted_list[mid] == value  return mid
        else:
            return mid
# loop ends return `False`
    return False


sorted_list = [1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9]
x = bi_search(sorted_list, 4)
print(x)