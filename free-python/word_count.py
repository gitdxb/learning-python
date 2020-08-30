import string
string.punctuation

fhandle = open('words.txt')
get_dict = dict()
for line in fhandle:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in get_dict:
            get_dict[word] = 1
        else:
            get_dict[word] = get_dict[word] + 1
lst = list(get_dict.keys())
#print(lst)
lst.sort()
for key in lst:
    print(key, get_dict[key])