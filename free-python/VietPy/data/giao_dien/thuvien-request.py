from requests import session
import re
s=session()
email= 'hoangminhdung'
DL=s.get('https://signup.live.com/signup?username='+email+'@hotmail.com&lic=1')
# print(DL.text)

kq=re.search("isAvailable",DL.text)
print(kq)

if kq==None:
    print("Còn sống")
else:
    print("Đã chết")