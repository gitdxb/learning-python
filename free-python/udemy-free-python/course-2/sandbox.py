#Given a string, return a string where for every character in the original, there are two characters.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'
#SOLUTION:

def doubleChar(str):
    result = ' '
    for char in str:
             result += char * 2
    return result
print(doubleChar('The'))