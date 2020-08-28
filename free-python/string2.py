# Take only email domain

str = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

getat = str.find('@')
print(getat)
getspace = str.find(' ',getat)
print(getspace)
get_domain = str[getat+1:getspace]
print(get_domain)