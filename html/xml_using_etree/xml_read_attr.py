
from xml.etree.ElementTree import Element, SubElement, dump
import xml.etree.ElementTree as et


note = Element("note")
note.attrib["date"] = "20120104"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"


res = note.getiterator('heading')

for it in res:
    print('{} : {} : {}'.format(it, it.text, it.items()))




# tree = et.ElementTree(note)
# tree.write('output.xml')
