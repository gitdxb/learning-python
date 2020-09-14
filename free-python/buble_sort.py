my_list = [5,9,5,8,1,3]

def bubble_sort(unsorted):
    sorted = unsorted[:]
    swapped = True
    while swapped == True:
        for i in range(len(sorted) - 1):
            if sorted[i] > sorted[i+1]:
                sorted[i], sorted[i+1] = sorted[i+1], sorted[i]
                print(sorted)


bubble_sort(my_list)
