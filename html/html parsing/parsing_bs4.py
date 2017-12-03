
import html

from bs4 import BeautifulSoup

# content = open('output.html', 'r').read()
# soup = BeautifulSoup(content, 'lxml')
#
# tag = soup.find('script_here')
#
#
# res_string = ''
#
# for it in tag:
#     res_string += str(it)
#
# # print(res_string)
#
with open('psutil.html','r') as file:
    content2 = file.read()

soup2 = BeautifulSoup(content2, 'html.parser')
tag_selected = soup2.find('head.title')

print(tag_selected)

# tag_selected.string = res_string
#
# rep = html.unescape(str(soup2))
#
# with open('psutil.html', 'w') as file:
#     file.write(rep)



# tag.string = 'new title here!!!!'
#
# tag = soup.find('table',{'id':'my_table'})
# tag.string = 'new value here!!!!'
#
#
# with open('sample2.html','r') as file:
#     content = file.read()
#
# content = content.replace('#script_here', str(soup))
#
# with open('output.html', 'w') as file:
#     file.write(content)
