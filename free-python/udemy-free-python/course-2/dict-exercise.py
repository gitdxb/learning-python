#Counting the number of each character in the paragraph



str = "It is a long established fact that a reader will be distracted by \
the readable content of a page when looking at its layout. The point of \
using Lorem Ipsum is that it has a more-or-less normal distribution of \
letters, as opposed to using 'Content here, content here', making it \
look like readable English. Many desktop publishing packages and web page \
editors now use Lorem Ipsum as their default model text, and a search for \
'lorem ipsum' will uncover many web sites still in their infancy. Various \
versions have evolved over the years, sometimes by accident, sometimes \
on purpose (injected humour and the like)."

##Declare to use dictionaries
characters = {}


#loop through str to access key and get value
for char in str:
    characters[char] = characters.get(char, 0) + 1  #insert the key for each characters with 'char'
print(characters)

#NOTE: So characters[char] is the key, and normally characters.get('key') to get value. +1 above is to add to default number