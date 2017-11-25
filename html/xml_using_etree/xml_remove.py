
from xml.etree.ElementTree import Element, SubElement, dump
import xml.etree.ElementTree as et

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


xml = open('input.xml').read()
root = et.fromstring(xml)


# add subelement
_Element = Element('age', {'loc':'Boston'})
_Element.text = '23'

info = root.findall("info[@id='2nd']")

for _info in info:
    addrs = _info.findall("addr")
    for addr in addrs:
        addr.append(_Element)



# # remove element
# info = root.findall("info[@id='1st']")
#
# for _info in info:
#     addrs = _info.findall("addr")
#     for addr in addrs:
#         _info.remove(addr)


indent(root)

dump(root)

tree = et.ElementTree(root)
tree.write('output.xml')
