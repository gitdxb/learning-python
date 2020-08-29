# Write your code here :-)
# Get number of items
shopping = []
count = 0
get_num = int(input('How many items for your shopping today? '))
for item_num in range(get_num):
    item = input("Item " + str(item_num) + ": " )
    shopping.append(item)
    count += 1

print('Total items: ', count)
print ("Here is your list : " + ', '.join(shopping))


