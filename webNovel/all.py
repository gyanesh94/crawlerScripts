#!/usr/bin/python

"""
1. Against The God
2. Skyfire Avenue
3. Martial God Asura
4. The Great Ruler
5. Tales Od Demons And Gods
6. Coiling Dragon
7. I Shall Seal the Heavens
8. Chaotic God Sword (Beware Of Comments)
8. Desolate Era
9. Stellar Transformations
"""

from bs4 import BeautifulSoup
import sys
import getopt
import re
import requests


url_list = [
    ["atg", "http://www.wuxiaworld.com/atg-index/atg-chapter-{}/"],
    ["csg", "http://gravitytales.com/chaotic-sword-god/csg-chapter-{}/"],
    ["col", "http://www.wuxiaworld.com/col-index/col-volume-9-chapter-{}/"],
    ["hjc", "http://www.wuxiaworld.com/hjc-index/hjc-chapter-48-{}/"],
    ["issth", "http://www.wuxiaworld.com/issth-index/issth-book-4-chapter-{}/"],
    ["mga", "http://www.wuxiaworld.com/mga-index/mga-chapter-{}/"],
    ["tdg", "http://www.wuxiaworld.com/tdg-index/tdg-chapter-{}/"],
    ["de", "http://www.wuxiaworld.com/desolate-era-index/de-book-12-chapter-{}/"],
    ["pw", "http://www.wuxiaworld.com/pw-index/pw-chapter-{}/"],
    ["tgr", "http://www.wuxiaworld.com/tgr-index/tgr-chapter-{}/"],
    ["wdqk", "http://www.wuxiaworld.com/wdqk-index/wdqk-chapter-{}/"],
    ["tmw", "http://gravitytales.com/true-martial-world/tmw-chapter-{}/"],
    ["God and devil", "http://www.translationnations.com/translations/god-and-devil-world/god-and-devil-world-chapter-0{}/"]
]


def get_url():
    url = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:")
    except getopt.GetoptError:
        print "Command Line Error"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-u':
            url = arg
    return url


# def get_src(url):
#     opener = urllib2.build_opener()
#     opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#     return opener.open(url)


def get_src(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def str_encode(name):
    name = name.strip()
    name = name.replace(':', '-')
    name = name.encode(encoding='unicode_escape')
    name = name.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", '--')
    name = name.decode(encoding='unicode_escape')
    return name


def url_encode(url):
    url = url.strip()
    url = url.encode(encoding='unicode_escape')
    url = url.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return url


def get_chapters(chapters):
    links = []
    for chapter in chapters:
        href = chapter['href']
        href = url_encode(href)
        name = chapter.string
        name = str_encode(name)
        links.append([href, name])
    return links


def save_chapter(name, content):
    # name= "/Users/gyanesh/Documents/.a/Web Novel alias/" + name
    # name = "/Users/gyanesh/Google Drive/Web Novels/Web Novel alias/" + name
    # name = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/" + name
    name = "./" + name
    text = open(name + ".txt", "w")
    text.write(content)
    text.close()


def get_content(url):
    src = get_src(url)
    soup = BeautifulSoup(src, 'html.parser')
    div = soup.find("div", {"class": "entry-content"})
    p = div.find_all("p")
    p = p[1:]
    # Name Extraction
    name = p[0]
    name = name.get_text()
    name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"  ", u" ").replace(u"  ", u" ")
    name = re.sub(r':', '-', name)
    name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name)
    name = re.sub(r'^0', '', name)
    name = name.strip()

    # Body Extraction
    p = p[1:]
    content = ""
    for i in p:
        if i.sup:
            if i.sup.a:
                i.sup.a.unwrap()
            i.sup.unwrap()
        if i.strong:
            i.strong.unwrap()
        if i.em:
            i.em.unwrap()
        t = i.get_text()
        t = t.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"  ", u" ")
        t = re.sub(r'^\s*', r'', t)
        t = re.sub(r'\s*$', r'', t)
        content += t + "\n\n"
    content = content.replace(u"\xa0", u" ")
    content = content.replace(u"\u3000", u" ")
    # content = re.sub(r'^(Edited|Translated)\sby\s?:\s?.*$\n*', '', content)
    content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*Next\sChapter([\S\w\W\s]*)', r'\1\n\3', content)
    content = re.sub(r'([\w\W\s\S]*)\[Previous\sChapter\][\s]*\[Table\sof\sContents\][\s]*\[Next\sChapter\]([\S\w\W\s]*)', r'\1\n\2', content)
    content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*\|[\s]*Index[\s]*\|[\s]*Next\sChapter([\S\w\W\s]*)', r'\1\n\3', content)
    content = re.sub(r'([\w\W\s\S]*)\>\s*Teaser\s*for\s*Next\s*Chapter\s*\<([\S\w\W\s]*)', r'\1\n\2', content)
    content = re.sub(r'\n\n[\n]+', r'\n\n', content)
    content = content.strip()

    # Foot note Extraction
    foot = soup.find("div", {"class": "footnotes"})
    if foot:
        content += "\n\n" + "-----------" + "\n"
        lis = foot.find_all("li")
        i = 1
        for li in lis:
            if li.span:
                li.span.decompose()
            content += str(i) + "." + li.get_text() + "\n"
            i += 1
        content = content.strip()
    return name, content.encode("utf-8")


def get_urls():
    i = 0
    for temp in url_list:
        print i, temp[0]
        i = i + 1
    url = url_list[input("Index= ")][1]
    start = input("Start= ")
    end = raw_input("End= ")
    if end == "":
        end = start
    else:
        end = int(end)
    l = []
    for i in range(start, end + 1):
        l += [url.format(i)]
    return l

urls = get_urls()

# urls = [get_url()]

for url in urls:
    name, content = get_content(url)
    save_chapter(name, content)
