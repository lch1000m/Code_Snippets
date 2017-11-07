
import bs4
from bs4 import BeautifulSoup

xml = open('file.xml').read()

soup = BeautifulSoup(xml, 'html.parser')

for e in soup.find_all('elem'):
    if e.text not in ['1','2']:
        e.extract()

with open('output.txt', 'w') as file:
    file.write(str(soup))
