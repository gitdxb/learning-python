## Course: https://www.udemy.com/course/learn-python-programming-and-cryptocurrency-data-analysis/learn/lecture/11692710#overview

# num = input("enter a number: ")
# print("You just enter: " + num)




#How to receive multiple input from user
 ##1
# list = [ x for x in input("Enter four numbers seperated by space: ").split()]
# print(list)

#So use split() to seperate each input by a space, use [] to output a list. For each x number enter, put x in the list. Out put will be strings


##2 Seperate by comma
# list = [ x for x in input("Enter four numbers seperated by comma: ").split(",")]
# print(list)

##3 change input to interger int(), or float()
# list = [ float(x) for x in input("Enter four numbers seperated by space: ").split()]
# print(list)

# Write a program to accept words and sort them alphabetically

# words = [x for x in input("Enter four awesome words by comma: ").split(",")]
#
# words.sort()
# print(words) #happy, amazing, beautiful, awesome

#print unique words, not duplicate

items = input("Enter some words by comma: ")
a = items.split(",")

print(", ".join(sorted(set(a))))


#set() to remove duplicate words