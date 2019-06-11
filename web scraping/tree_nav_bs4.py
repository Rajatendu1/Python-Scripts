from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
#Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print ("Retrieving: ",url)
html = urlopen(url,context=ctx).read()
print ("Retrieved: ",len(html))
tree = ET.fromstring(html)
results = tree.findall('.//comment')
total = list()
for result in results:
    num = result.find('count').text
    num_int = int(num)
    total.append(num_int)
print ("Sum:",sum(total))
