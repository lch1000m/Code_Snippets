
# parsing html by etree

from xml.etree.ElementTree import ElementTree

parser = ElementTree()

parser.parse('output.html')

parser.find('body/table').text = "contents changed!"

parser.write('output.html')

# # replace tag's attr
# p = parser.find('body/p')

# for lk in p.iter('a'):
#     p.attrib['target'] = 'blank'
