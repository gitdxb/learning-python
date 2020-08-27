# function
def print_lyric():
    print("Something goes here 1")
    print("Then something goes here too 2")

def repeat_lyric():
    print_lyric()
    print_lyric()


# repeat_lyric()

def print_twice(bruce):
    print(bruce)
    print(bruce)

# print_twice()

def addtwo(a,b):
    #return a + b
    added = a + b
    return added
x = addtwo(2,3)
#print(x)
#get_hours = input("Enter hours: ")
#get_rate = input("Enter rate: ")
try:

    hours = float(get_hours)
    rate = float(get_rate)
except:
    print("Please enter numeric input")

def computepay(hours,rate):
    if hours > 40:
        reg = 40 * rate
        otp = (hours - 40) * 15
        pay = reg + otp
        print("Your pay is: ",pay)
    else:
        pay = hours * rate
        print("Your pay: ",pay)
# computepay(hours, rate)

# Greeting
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


while True:
    line=input('> ')
    if line=='done':
        break
    print(line)
print('Done!')
