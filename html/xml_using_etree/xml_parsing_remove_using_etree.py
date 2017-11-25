
import xml.etree.ElementTree as et


xml = open('input.xml').read()
root = et.fromstring(xml)


# search = root.findall('to')
#
# for child in search:
#     child.text = 'changed!'


search = root.find('to')
search.text = 'changed!'



tree = et.ElementTree(root)
tree.write('output.xml')
