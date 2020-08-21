#List comprehension


#declare a list
#a = []

#for i in range(1,11):
#    a.append(i)
#print(a)

#Shorter version
#a = [i for i in range(1,11)]  #for i in range 1 to 11, return to i

#print(a)

#Write a program to find common items from 2 lists
a = [2,4,56,87,23,786,98]
b = [2,34,7,56,67]

result = []

for i in a:
    if i in b:
        result.append(i)

#[result.append(i) for i in a if i in b]
#result = [i for i in a if i in b]

print(result)