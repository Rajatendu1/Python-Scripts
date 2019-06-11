import json
from urllib.request import urlopen
import ssl

#Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print ("Retrieving: ",url)
data = urlopen(url,context=ctx).read()
print ("Retrieved: ",len(data))
info = json.loads(data)["comments"]
print('User count:', len(info))

sum = 0
for item in info:
    num = item["count"]
    num_int = int(num)
    sum += num_int
print ("Sum: ", sum)
