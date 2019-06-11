from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

#Retrieve all of the anchor tags

tags = soup('span')
total = 0
for tag in tags:
    # Look at the parts of the tag
    num = tag.contents[0]
    num_int = int(num[0:])
    total+= num_int
print (total)
    #Retrieve number with positions 0 onwards
