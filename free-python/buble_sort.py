my_list = [5,9,5,8,1,3]

def bubble_sort(unsorted):
    sorted = unsorted[:]
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(sorted) - 1):
            if sorted[i] > sorted[i+1]:
                sorted[i], sorted[i+1] = sorted[i+1], sorted[i]
                swapped = True
    return sorted

print('Before:', my_list)
print('After:',bubble_sort(my_list))
