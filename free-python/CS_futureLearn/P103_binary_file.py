data = [100,24,255]
buffer = bytes(data)
print(buffer)
f = open('binary.txt','bw')
f.write(buffer)
f.close()

f = open('binary.txt', 'br')
binary = f.read()
print(binary)
data = list(binary)
print(data)
f.close()