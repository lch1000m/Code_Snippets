
import xml.etree.ElementTree as et


xml = open('file.xml').read()

root = et.fromstring(xml)

section = root.findall('query')

num = ['1']

for sub in section:
    for child in sub[::-1]:
        if child.text in num:
            sub.remove(child)

tree = et.ElementTree(root)
tree.write('output.xml')
