print('Temperature converter')
print('=====================')
get_c = input("What is the temperature in Celsius? ")

convert_c = int(get_c)
print_f = convert_c * 9 / 5 + 32

print("The temperature in F is {}°F".format(int(print_f)))

if convert_c > 40:
    print("OMG! It's so hot! Don't forget to drink more water!")