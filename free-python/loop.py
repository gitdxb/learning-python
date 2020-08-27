'''
while True:
    a = input("First num: ")
    b = input("Second num: ")
    if a == 'ok' or b == 'ok':
      break
    else:
        print(int(a) + int(b))
'''

'''
# Đếm số item trong 1 list
count=0
item = [3,41,12,9,74,15]
for i in item:
    count=count+1
print('Count: ', count)
'''
'''
#Công thức tính tổng
total=0
for itervar in [3,41,12,9,74,15]:
    total=total+itervar
print('Total: ', total)
'''
# tìm giá trị lớn nhất
largest = None
print("Largest: ", largest)
for i in [3,41,12,0,9,74]:
   if largest is None or i > largest:
       largest = i
   print('Loop: ', i, largest)
print("Largest: ", largest)