
from requests import session
import re
s=session()
email= ''
DL=s.get('')
# print(DL.text)

kq=re.search("isAvailable",DL.text)
print(kq)

if kq==None:
    print("Còn sống")
else:
    print("Đã chết")