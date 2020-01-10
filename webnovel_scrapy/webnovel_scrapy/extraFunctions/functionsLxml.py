import re
from lxml import etree


def parseHtml(src):
    htmlParser = etree.HTMLParser(encoding="utf-8")
    return etree.HTML(src, htmlParser)


def printHtml(html):
    result = etree.tostring(html, pretty_print=True, method="html")
    print(result)


def getText(html):
    text = etree.tostring(html, encoding="utf-8", method="text")
    text = text.decode('utf-8', 'ignore')
    return text


def formatName(name):
    name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\xe2", u" ")
    name = name.replace(u"\u2013", u"-").replace("@", " ").replace(";", "").replace("\\", "-").replace("/", "-")
    name = name.replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"')
    name = name.replace("*", " ").replace(":", "-")
    name = name.replace("<", "").replace(">", "")
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'^\.', '', name)
    return name.strip()


def encodeName(name):
    name = name.encode('utf-8', 'ignore')
    return name
