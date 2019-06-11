from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
num = input('Enter count: ')
pos = input('Enter position: ')

print ("Retrieving: ",url)
for times in range(int(num)):
    html = urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    print ("Retrieving: ",tags[int(pos)-1].get('href',None))
    url =  tags[int(pos)-1].get('href',None)
