import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name',tree.find('name').text)
print('Attr', tree.find('email').get('hide'))

hand = open('README.md','w')
hand.write('These codes are part of PY4E course by Dr Chuck\n')
hand.write('For more info, visit: https://py4e.com')
hand.close()