
from xml.etree.ElementTree import Element, SubElement, dump
import xml.etree.ElementTree as et

note = Element("note", name="CH Lee")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"
note.attrib["date"] = "20120104"
note.attrib["id"] = "Unique"


tree = et.ElementTree(note)
tree.write('output.xml')
