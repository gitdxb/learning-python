# r: Chế độ chỉ đọc (khi có dữ liệu sẵn)
# a: Chỉ ghi (Ko xoá data cũ, ghi thêm dòng mới)
# w: Chỉ ghi (xoá dữ liệu cũ và ghi đè lên)
# r+:
# a+:
# w+:
#ghi
file = open('test2.txt', 'w')
file.write("Some dummy text")

#read
# file = open('test.txt', 'r').read()
# print(file.split('\n')[0].split(',')[3])
# print(file.split('\n')[1].split(',')[3])
# print(file.split('\n')[2].split(',')[3])
# print(file.split('\n')[3].split(',')[3])
# print(file.split('\n')[4].split(',')[3])
# Neu file.split('\n')[0] se print ra mang

#vong lap
file = open('test.txt', 'r').read()
mang_acc = file.split('\n')
file_cookie = open('test2.txt', 'w')
for x in mang_acc:
    file_cookie.write(x.split(',')[3] + '\n')


