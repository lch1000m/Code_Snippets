
from bs4 import BeautifulSoup

content = open('sample.html', 'r').read()
soup = BeautifulSoup(content, 'lxml')


tag = soup.find('title')
tag.string = 'new title here!!!!'


tag = soup.find('table',{'id':'my_table'})
tag.string = 'new value here!!!!'



print(soup)

with open('output.html', 'w') as file:
    file.write(str(soup))
