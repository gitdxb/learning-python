#if statement

#Turn light on and off

light = False

if light:
    light = False
else:
    light = True
print(light)

##The above code the same with 'light = not light'. output: false


# Odd or even number
a = int(input("Please enter a number: ")) #Use int() to convert input to interger

if a % 2 == 0:
    print("You just entered an even number!")
else:
    print("That is an odd number!")


#FOR STATEMENT
for number in range(1,11):
    print(number)

_list = [True, 123,1212,345,1212,42, "tomorrow"]

for items in _list:
    print(items)

#Or print only first 5 items
#for items in _list[:5]
#    print(items)

#find top 3 value items
_list = [1,2,3,5,7,87,12,4323,653,999,343,88888,32,0,23]
max1 = max2 = max3 = min(_list)

for x in _list:
    if x > max3:
        max1 = max2
        max2 = max3
        max3 = x
    elif x > max2:
        max1 = max2
        max2 = x
    elif x > max1:
        max1 = x
print(max1)
print(max2)
print(max3)
#write a program that checks if a list contains a sublist

a = [7,11,23,34,56,89,1]
b = [23,34]
is_sub_list = False

for i in range(len(a)):
    if(a[i] == b[0]):
        n = 1
        while(n < len(b)) and a[i + n] == b[n]:
            n += 1

        if(n == len(b)):
            is_sub_list = True
print(is_sub_list)

#Continue condition
for i in rang(1,11):
    if i % 2 == 0:
        continue
    print(i)