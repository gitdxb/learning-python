import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

tree = ET.fromstring(input)
lst = tree.findall('users/user')
print('User count',len(lst))


for item in lst:
    print('User name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attr:', item.get('x'))