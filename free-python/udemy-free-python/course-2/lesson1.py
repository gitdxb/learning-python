a = 5

if a == 5:
    print(a)


s = sum([1,2,3])
print(s)

#Check data type
number = str(5)
print(number)
print(type(number))

#switch value
a = 5
b = 10

temp = a
a = b
b = temp
#Or
a ,b = b, a
print(a)
print(b)

"""
THIS
IS MULTIPLE LINE
COMMENT
"""

#if statement
a, b = 7, 10
print( a == b )
print( a != b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#logical operators
a=1
b=9

print((a == 2 and b == 9))
print((a == 2 or b == 1))
print(not(a == 2 or b == 1))

#Create a new file and create content in it
file=open('text.txt', 'w')
file.write("Hello world \n")
file.write("This is another paragraph")

#Sum
a = 4
b = 10
print("Total sum is: " , a + b)
#print function

a,b = 10, 11
print(a,b)
#or
print(a,b, sep='====')
#Print method
name = "Adam"
mark = 49.6454
print("Name is: ",name, ".Mark is: ",mark)
print("Name is %s, Mark is %.2f "%(name,mark))

print("Name is {}, mark is {}".format(name,mark))
print("Name is {0}, mark is {1}".format(name,mark))

#Working with strings
str1 = "Python "
str2 = "is a great programming language"
print(str1 + str2)
print(str1[:2]) #print first 2 characters
print(str1[:-2]) #print whole string without last 2 characters
print(str1[2:]) #print whole string without first 2 char
print(str1[-2:]) #print only the last 2 char
print(str1[1::2]) #from char 1 print the 2nd char each 1 jump



#Print "Python is the best programming language in the world" from 3 strings

string_one = "You are learning Python"
string_two = "There are 256 programming languages in the world."
string_three = "You are the best"

result = string_one[-6:] + string_two[-14:-12] + string_three[-2] + string_three[-9:] \
         + string_two[13:34] + string_two[-14:]

print(result)


#String method, search method

string1 = "Python"
string2 = " is the great programming language in the world"

print(string2.find('great')) #position 8

#count how many character 'i'
print(string2.count('i')) #3
print(string2.split(" ")) #split the string with every space
print(string2.replace("great", "amazing")) #replace great with amazing

#concatenate 2 different data type
a = "Number "
b = 7
#print(a + b) #output will be false
print(a + str(b))


#Working with list
list1 = [1,2,3,4,5,5.6,"Asma", True]
print(list1)
print(list1[1])
print(list1[1:4])  #only print from index 1 to 3
print(len(list1))

#Calculate the average
a = [1,2,3,4,5,6]
print(sum(a)/len(a)) #output: 3.5

#Manipulate list
list_one = [1,2,3,4,5,6,"JS", "C++"]
list_one.append("Python")
list_one.append(10)
list_one.insert(1,11) #insert no 11 to position 1
list_one[1] = 14
list_one.remove("JS")
#list_one.pop() => delete last item
#print(list_one.pop()) => bring a item back
#list_one.pop(1) , delete item index 1
print(list_one)

# List and range method
list1 = list(range(1,11))
#Reverse range: list2 = list(range(30,1,-2)


list1 += [3,223,21,432]

#min print(min(list1)) ====> if the list only contain number or string, not mix
#max print(max(list1))

#to sort
list1.sort()
#or
list1.sort(reverse=True)
list1.reverse()
print(list1)

#List sort and reverse
data = ["abc", "basda", "cefd","da","e"]
result = reversed(data) #make a copy and in reverse order, otherwise data.reverse()


print(data)
print(list(result))  #reverse a list

#Sorting
data = ["abc", "basda", "cefd","da","e"]
#data.sort()

#or
result = list(sorted(data))

print(data)
print(result)

#SOrt by length and reverse
data = ["abc", "basda", "cefd","da","e"]

result = list(sorted(data, key=len, reverse=True))

print(result)