# Adding new list item and check if it's duplicated

name_list = ['Fatima', 'Hasan', 'Dush']
while True:
  new_name = input('Enter a name to add > ')
  if new_name in name_list:
      print ('Sorry, that name is already in the list')
      continue
  else:
      name_list.append(new_name)
  print (name_list)