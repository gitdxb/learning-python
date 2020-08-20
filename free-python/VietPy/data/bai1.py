# r: Chế độ chỉ đọc (khi có dữ liệu sẵn)
# a: Chỉ ghi (Ko xoá data cũ, ghi thêm dòng mới)
# w: Chỉ ghi (xoá dữ liệu cũ và ghi đè lên)
# r+:
# a+:
# w+:

file = open('data/test.txt', 'w')
file.write('Hoc python mien phi')
file.write('haha')
