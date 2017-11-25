
import xml.etree.ElementTree as et

root = et.fromstring("""
<root>
    <articles>
        <article type="news">
             <content>some text1</content>
        </article>
        <article type="info">
             <content>some text2</content>
        </article>
        <article type="news">
             <content>some text3</content>
        </article>
    </articles>
</root>
""")

articles = root.find("articles")
article_list = articles.findall("article[@type='news']/content")
for a in article_list:
    print(a.text)
