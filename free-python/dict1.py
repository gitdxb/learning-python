ddd = {'one':'uno', 'two':'dos','three':'tres'}

# Access the key/value pair
ddd['one'] # uno

# Access value only
ddd.values()

# And print to a list
list(ddd.values())

# Check if a value is in a dict
val = list(ddd.values())
'uno' in val #True