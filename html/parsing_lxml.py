
# parsing html by lxml

import lxml.html
from lxml.cssselect import CSSSelector


html = open('output.html').read()

tree = lxml.html.fromstring(html)

selector = CSSSelector('#myid')

selection = selector(tree)

selector.text = 'new value~~~!'
