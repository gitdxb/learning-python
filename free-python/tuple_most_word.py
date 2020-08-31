fname = input('Enter file: ')
if len(fname) < 1: fname ='words.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

#print(di)
tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)
#print('Flipped \n', tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted \n',tmp[:5])

for v,k in tmp[:5]:
    print(k,v)