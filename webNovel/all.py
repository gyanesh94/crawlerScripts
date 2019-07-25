# -*- coding: utf-8 -*-
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
import argparse
import re
import signal
import os
import requests
import cfscrape
import time
from listings_download import *
from multiprocessing import Pool

SKIP_DEFAULT = True
MAKE_P_RECURSICE = False

if LIST_TRUE or SKIP_DEFAULT:
    SAVE_DIRECTORY = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/"
else:
    SAVE_DIRECTORY = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/"

if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

url_list = [
    ["Invincible", "https://www.wuxiaworld.com/novel/invincible/inv-chapter-{}"],
    ["Talisman Emperor", "https://www.wuxiaworld.com/novel/talisman-emperor/te-chapter-{}"],
    ["Renegade Immortal", "https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-{}"],
    ["Spirit Realm", "https://www.wuxiaworld.com/novel/spirit-realm/sr-chapter-{}"],
    ["Ancient Strengthening Technique", "https://www.wuxiaworld.com/novel/ancient-strengthening-technique/ast-chapter-{}"],
    ["SYWZ", "http://gravitytales.com/novel/shen-yin-wang-zuo/sywz-chapter-{}"],
    ["Against the Gods", "http://www.wuxiaworld.com/atg-index/atg-chapter-{}/"],
    ["Chaotic Sword God", "http://gravitytales.com/chaotic-sword-god/csg-chapter-{}/"],
    ["Emperor's Domination", "http://www.wuxiaworld.com/emperor-index/emperor-chapter-{}/"],
    ["Legend of the Dragon King", "http://www.wuxiaworld.com/ldk-index/ldk-chapter-{}/"],
    ["Martial God Asura", "http://www.wuxiaworld.com/mga-index/mga-chapter-{}/"],
    ["Perfect World", "http://www.wuxiaworld.com/pw-index/pw-chapter-{}/"],
    ["Sovereign of the Three Realms", "http://www.wuxiaworld.com/sotr-index/sotr-chapter-{}/"],
    ["The Great Ruler", "http://www.wuxiaworld.com/tgr-index/tgr-chapter-{}/"],
    ["Dragon Maken War", "https://www.wuxiaworld.com/novel/dragon-maken-war/dmw-chapter-{}"],
    ["OverGeared", "https://www.wuxiaworld.com/novel/overgeared/og-chapter-{}"],
]


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    exit()


def get_url():
    parser = argparse.ArgumentParser(description='Fetch Url')
    parser.add_argument('-u', action="store", default=None, dest='url', help="give url")
    url = parser.parse_args().url
    return url


def get_src(url):
    r = requests.get(url)
    if r.status_code == 503:
        print "test"
        scraper = cfscrape.create_scraper()
        s = scraper.get(url)
        s.encoding = 'utf-8'
        return s.text
    elif r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    exit()


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


def save_chapter(name, content, url):
    if url.find("/novel/ancient-strengthening-technique/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Ancient Strengthening Technique/"

    elif url.find("/novel/dragon-maken-war/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Dragon Maken War/"

    elif url.find("/novel/invincible/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Invincible/"

    elif url.find("/novel/overgeared/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Overgeared/"

    elif url.find("/novel/renegade-immortal/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Renegade Immortal/"

    elif url.find("/novel/spirit-realm/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Spirit Realm/"

    elif url.find("/novel/stop-friendly-fire/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Stop, Friendly Fire!/"

    elif url.find("/novel/talisman-emperor/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Talisman Emperor/"

    elif url.find("/novel/upgrade-specialist-in-another-world/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Upgrade Specialist in Another World/"

    elif url.find("/novel/martial-god-asura/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Slow_Stopped/Martial God Asura/"

    elif url.find("/novel/the-great-ruler/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Slow_Stopped/The Great Ruler/"

    else:
        path = SAVE_DIRECTORY
    name = os.path.join(path, name)
    text = open(name + ".txt", "w")
    text.write(content)
    text.close()


def get_content(url, getName=""):
    print url
    src = get_src(url)
    soup = BeautifulSoup(src, 'lxml')
    p = []
    div = soup.find("div", {"class": "entry-content"})
    if div is not None:
        if url.find("www.wuxiaworld.com/emperor-index") != 1:
            if div.find('div', {"class": "sp-wrap"}) is not None:
                div.find('div', {"class": "sp-wrap"}).decompose()
        p = div.find_all("p")
    # For God and Devil world novel extra line Novel
    # if url.find('http://www.translationnations.com') != -1:
    #    p = p[1:]
    if url.find('gravitytales.com') == -1:
        p = p[1:]

    # Name Extraction
    if SKIP_NAME and LIST_TRUE:
        name = re.sub(r':', '-', getName, flags=re.IGNORECASE)
        name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^0', '', name, flags=re.IGNORECASE)
        name = name.strip()
    else:
        if url.find('novelfull.com/') != -1:
            div = soup.find('div', {"id": "chapter-content"})
            
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            while p[0].get_text().strip() == "":
                del p[0]
            name = p[0]
            del p[0]

        elif url.find('novel/martial-world/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            while p[0].get_text().strip() == "":
                del p[0]
            if re.search(r'^.*Chapter [0-9]{1,3}.*$', p[0].get_text(), flags=re.IGNORECASE):
                name = p[0]
                del p[0]
            else:
                temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
                temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
                temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
                temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
                if temp_chapter_name == temp_chapter_name_in_body:
                    print "equals"
                    name = p[0]
                    del p[0]

        elif url.find('novel/ancient-strengthening-technique/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 6:
                div = divUpper.find('div', {"id": "chapterContent"})
                p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if re.findall('(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()) != []:
                print(re.findall('(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()))
                name = p[0]
                del p[0]
            else:
                temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
                temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
                temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
                temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
                if temp_chapter_name == temp_chapter_name_in_body:
                    print "equals"
                    name = p[0]
                    del p[0]

        elif url.find('novel/stop-friendly-fire/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 10 and url.find('novel/stop-friendly-fire') != -1:
                p = div.find_all("div", recursive=MAKE_P_RECURSICE) + p

            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
            if temp_chapter_name == temp_chapter_name_in_body:
                print "equals"
                name = p[0]
                del p[0]

        elif url.find('wuxiaworld.com') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            while p[0].get_text().strip() == "":
                del p[0]
            # print name.get_text()
            # print p[0].get_text()
            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
            if temp_chapter_name == temp_chapter_name_in_body:
                print "equals"
                name = p[0]
                del p[0]
        elif url.find('wdqk-index') != -1:
            temp = p[0]
            if temp is not None and temp.get_text().find('Chapter') != -1:
                name = temp
                del p[0]
            else:
                name = soup.find("h1", {"class": "entry-title"})
        elif url.find('mga-index') != -1:
            name = p[0].strong.extract()
        elif url.find('chaotic-sword-god') != -1:
            temp = p[0]
            if temp is not None and temp.get_text().find('Chapter') != -1:
                name = temp
                del p[0]
            else:
                name = soup.find("h4")
        elif url.find('webnovel.com') != -1:
            nameDiv = soup.find('div', {"class": "cha-tit"})
            name = nameDiv.h3
            div = soup.find('div', {"class": "cha-words"})
            p = div.find_all("p", recursive=False)
        else:
            name = p[0]
            del p[0]
        name = name.get_text()
        if url.find('warlock-of-the-magus-world') != -1:
            temp_name = p[0].get_text().encode('utf-8')
            name = "{} - {}".format(name, temp_name)
            name = name.decode('utf-8')
            del p[0]
        if url.find('perfect-world') != -1:
            name = p[0].get_text()
            del p[0]
        name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"')
        name = re.sub(r' [ ]+', r' ', name)
        while not name or name == " " or name == "":
            name = p[0]
            del p[0]
            name = name.get_text()
            name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"')
            name = re.sub(r' [ ]+', r' ', name)
        name = re.sub(r':', '-', name)
        if url.find('novel/stop-friendly-fire') != -1:
            name = name.replace(">", "").replace("<", "")
        name = name.split("Chapter")
        if len(name) > 1:
            del name[0]
        name = "Chapter".join(name)
        # name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name, 1)
        name = re.sub(r'^AST ([0-9]{1,5})', r'\1', name)
        name = re.sub(r'^0+', '', name)
        name = name.strip()
        if url.find('http://www.radianttranslations.com') != -1:
            tempName = url
            tempName = re.sub(r'^[\w\s\S\W-]*chapter-', '', tempName)
            tempName = tempName.replace(u"-", u".").replace(u"/", u"")
            name = tempName + " " + name

    # Body Extraction
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
        if i.br:
            t = i.get_text(separator="\n")
        else:
            t = i.get_text()
        tempLower = t.lower()
        if tempLower.find('patreon') != -1 and tempLower.find('support') != -1:
            break
        t = t.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"\u2013", u"-")
        t = re.sub(r'^\s*', r'', t)
        t = re.sub(r'\s*$', r'', t)
        t = re.sub(r'^ +$', r'', t)
        t = t.strip()
        if t == "":
            continue
        content += t + "\n\n"
    content = content.replace(u"\xa0", u" ")
    content = content.replace(u"\u3000", u" ")
    content = content.strip()

    # content = re.sub(r'^(Edited|Translated)\sby\s?:\s?.*$\n*', '', content)
    content = re.sub(r'([\w\W\s\S]*)Do you want to read up to [0-9]{1,2} unreleased chapters\? Support UTS on Patreon!', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)Advertisement\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)\>\s*Teaser\s*for\s*Next\s*Chapter\s*\<\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)This\s*Chapter.?s\s*Teaser\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)\[Previous\sChapter\][\s]*\[Table\sof\sContents\][\s]*\[Next\sChapter\]\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*\|[\s]*Index[\s]*\|[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)«(\s)?Previous(\sChapter)?[\s]*\|[\s]*Next\sChapter(\s)?»\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'([\w\W\s\S]*).Previous\s*Chapter[\s]*\|[\s]*Next\s*Chapter.?\Z', r'\1', content, flags=re.IGNORECASE)
    content = content.strip()
    content = re.sub(r'\n +\n', r'\n\n', content, flags=re.IGNORECASE)
    content = re.sub(r'\n\n[\n]+', r'\n\n', content, flags=re.IGNORECASE)
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

    if url.find('wuxiaworld.com') != -1:
        foot = soup.select('div[id*="footnote"]')
        if foot and len(foot) != 0:
            content += "\n\n" + "-----------" + "\n"
        for i in foot:
            p = i.find_all("p", recursive=False)
            if not p or p is None or len(p) == 0:
                continue
            for t in p:
                t = t.get_text()
                t = t.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"\u2013", u"-")
                t = re.sub(r'^\s*', r'', t)
                t = re.sub(r'\s*$', r'', t)
                t = re.sub(r'^ +$', r'', t)
                t = t.strip()
                content += t + "\n"
        content = content.strip()

    return name, content.encode("utf-8")


def download_chapter(url):
    name, content = get_content(url)
    save_chapter(name, content, url)


if LIST_TRUE:
    if SKIP_NAME:
        for l in LIST:
            name, content = get_content(l[0], l[1])
            save_chapter(name, content, l[0])
    else:
        if len(LIST) < 10:
            for url in LIST:
                name, content = get_content(url)
                save_chapter(name, content, url)
                time.sleep(1)
        else:
            pool = Pool(3)
            try:
                pool.map(download_chapter, LIST, chunksize=1)
            except KeyboardInterrupt:
                print("Caught KeyboardInterrupt, terminating workers")
                pool.terminate()
            else:
                print("Normal termination")
                pool.close()
            pool.join()
    exit()


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


tempUrl = get_url()

if LIST is not None and LIST != []:
    urls = LIST
elif tempUrl is None:
    urls = get_urls()
else:
    urls = [tempUrl]

signal.signal(signal.SIGINT, signal_handler)

if len(urls) < 10:
    for url in urls:
        name, content = get_content(url)
        save_chapter(name, content, url)
        time.sleep(1)
else:
    pool = Pool(3)
    try:
        pool.map(download_chapter, urls, chunksize=1)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
    else:
        print("Normal termination")
        pool.close()
    pool.join()
