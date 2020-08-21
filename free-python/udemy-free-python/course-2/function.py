def add(a,b):
    return a + b
print(add(2,3))

#lambda function
c = lambda a,b: a + b
print(c(2,3))

#find max

def compare(a,b):
    if a > b:
        return a
    else:
        return b
print(compare(2,3))

f = lambda a,b: a if a > b else b

print(f(3,10))

#odd or even

x = lambda a: "even" if a% 2 ==0 else "odd"

print(x(11))
print(x(8))

#filter a list

l = [1,2,3,334,212,5434]

result = list(filter(lambda a: a<300, l))
print(result)

#sort a list
l = [['Noad', 91.5], ['Mark', 95.5], ['Jayson', 90.5]]

l.sort(key=lambda a: a[1])

print(l)