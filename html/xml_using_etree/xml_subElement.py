
from xml.etree.ElementTree import Element, SubElement, dump
import xml.etree.ElementTree as et

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "From").text = "Jani"


dummy = Element("dummy")
note.insert(0, dummy)
note.remove(to)

tree = et.ElementTree(note)
tree.write('output.xml')


"""
result:
<note>
    <to>Tove</to>
    <from>Jani</from>
</note>
"""