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
from urllib.parse import urlsplit

SKIP_DEFAULT = False
MAKE_P_RECURSICE = False

if LIST_TRUE or SKIP_DEFAULT:
    SAVE_DIRECTORY = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/"
else:
    SAVE_DIRECTORY = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/"

if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

url_list = [
    ["A Record of a Mortal's Journey to Immortality", "https://www.wuxiaworld.com/novel/rmji/rmji-chapter-{}"],
    ["Ancient Strengthening Technique", "https://www.wuxiaworld.com/novel/ancient-strengthening-technique/ast-chapter-{}"],
    ["Imperial God Emperor", "https://www.wuxiaworld.com/novel/imperial-god-emperor/ige-chapter-{}"],
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
    ["Martial God Asura", "https://www.wuxiaworld.com/novel/martial-god-asura/mga-chapter-{}/"],
    ["Perfect World", "http://www.wuxiaworld.com/pw-index/pw-chapter-{}/"],
    ["Sovereign of the Three Realms", "http://www.wuxiaworld.com/sotr-index/sotr-chapter-{}/"],
    ["The Great Ruler", "http://www.wuxiaworld.com/tgr-index/tgr-chapter-{}/"],
    ["Dragon Maken War", "https://www.wuxiaworld.com/novel/dragon-maken-war/dmw-chapter-{}"],
    ["OverGeared", "https://www.wuxiaworld.com/novel/overgeared/og-chapter-{}"],
]


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    exit()


def print_html(html):
    print(html.prettify())


def get_url():
    parser = argparse.ArgumentParser(description='Fetch Url')
    parser.add_argument('-u', action="store", default=None, dest='url', help="give url")
    url = parser.parse_args().url
    return url


def get_src(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 503:
        print("test")
        scraper = cfscrape.create_scraper()
        s = scraper.get(url)
        s.encoding = 'utf-8'
        return s.text
    elif r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    exit()


def save_website(url, txt, name, save_path=HTML_SAVE_PATH, save_folder=HTML_FOLDER_NAME):
    url = urlsplit(url)
    domain = url.hostname
    novel_path = url.path[1:]
    if save_folder:
        novel_path = save_folder
    full_path = os.path.join(save_path, domain, novel_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    with open(os.path.join(full_path, name + ".html"), 'w') as chapter_file:
        chapter_file.write(txt)


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
    if url.find("/novel/rmji/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/A Record of a Mortal's Journey to Immortality/"

    elif url.find("/novel/ancient-strengthening-technique/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Ancient Strengthening Technique/"

    elif url.find('/novel/archfiend/') != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Archfiend/"

    elif url.find('/novel/city-of-sin/') != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/City of Sin/"

    elif url.find("/novel/dragon-maken-war/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Dragon Maken War/"

    elif url.find("/novel/gate-of-revelation/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Gate of Revelation/"

    elif url.find("/novel/imperial-god-emperor/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Imperial God Emperor/"

    elif url.find("/novel/invincible/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Invincible/"

    elif url.find("/novel/lord-of-all-realms/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Lord of All Realms/"

    elif url.find("/novel/renegade-immortal/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Renegade Immortal/"

    elif url.find("/novel/sage-monarch/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Sage Monarch/"

    elif url.find("/novel/spirit-realm/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Spirit Realm/"

    elif url.find("/novel/spirit-vessel/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Spirit Vessel/"

    elif url.find("/novel/stop-friendly-fire/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Stop, Friendly Fire!/"

    elif url.find("/novel/talisman-emperor/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Talisman Emperor/"

    elif url.find("/novel/the-charm-of-soul-pets/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/The Charm of Soul Pets/"

    elif url.find("/novel/the-godsfall-chronicles/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/The Godsfall Chronicles/"

    elif url.find("/novel/the-novels-extra/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/The Novel's Extra/"

    elif url.find("/novel/martial-god-asura/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Martial God Asura/"

    elif url.find("/novel/perfect-world/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Perfect World/"

    elif url.find("/novel/the-great-ruler/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/The Great Ruler/"

    elif url.find("/novel/the-unrivaled-tang-sect/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/The Unrivaled Tang Sect/"

    else:
        path = SAVE_DIRECTORY
    name = os.path.join(path, name)
    print(name)
    text = open(name + ".txt", "wb")
    text.write(content)
    text.close()


def replace_ul(elem, soup):
    ul_s = elem.find_all("ul", recursive=MAKE_P_RECURSICE)
    for ul in ul_s:
        new_elem = soup.new_tag("p")
        text = ""
        li_s = ul.find_all("li", recursive=MAKE_P_RECURSICE)
        for li in li_s:
            text = f"{text}- {li.get_text()}\n"
        text = text.strip()
        new_elem.string = text
        elem.ul.replace_with(new_elem)
        # print(ul)


def replace_hr(elem, soup):
    hr_s = elem.find_all("hr", recursive=MAKE_P_RECURSICE)
    for hr in hr_s:
        new_elem = soup.new_tag("p")
        new_elem.string = "-------"
        elem.hr.replace_with(new_elem)


def replace_em(elem, soup):
    em_s = elem.find_all("em", recursive=MAKE_P_RECURSICE)
    for em in em_s:
        text = em.get_text().replace(u'\u2060', ' ').replace(u'\xc2\xa0', ' ').replace(u'\xa0', ' ')
        if len(text):
            if text[-1] == " ":
                em.string = f"'{text[:-1]}' "
            else:
                em.string = f"'{text}'"


def get_content(url, getName=""):
    print(url)
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

    save_path = None
    save_folder = None
    # Name Extraction
    if SKIP_NAME and LIST_TRUE:
        name = re.sub(r':', '-', getName, flags=re.IGNORECASE)
        name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^0', '', name, flags=re.IGNORECASE)
        name = name.strip()
    else:
        if url.find('www.centinni.com/') != -1:
            div_header = soup.find('div', {"class": "entry-header"})
            li = div_header.find('li', {"class": "active"})
            if not li:
                exit()

            div_entry_content = soup.find("div", {"class": "entry-content"})
            div = div_entry_content.find("div", {"class": "text-left"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 8:
                p = div.find_all("p", recursive=True)
            while p[0].get_text().strip() == "":
                del p[0]

            name = li
            save_path = HTML_SAVE_PATH
            save_folder = "Long Live Summons"
        elif url.find('wangmamaread.com') != -1:
            h3 = soup.find('h3', {"class": "entry-title"})
            if not h3:
                exit()

            div = soup.find("div", {"class": "entry-content"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 8:
                p = div.find_all("p", recursive=True)
            while p[0].get_text().strip() == "":
                del p[0]

            name = h3
        elif url.find('comrademao.com/') != -1:
            div = soup.findAll(lambda tag:tag.name == "div" and len(tag.attrs) == 1 and re.search('^[0-9]+$', tag.get("readability", "")))
            if not div:
                exit()
            div = div[0]

            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 8:
                p = div.find_all("p", recursive=True)
            while p[0].get_text().strip() == "":
                del p[0]

            name = p[0]
            del p[0]
        elif url.find('novelfull.com/') != -1:
            div = soup.find('div', {"id": "chapter-content"})
            nameSpan = soup.find('span', {"class": "chapter-text"})
            
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 8:
                p = div.find_all("p", recursive=True)
            while p[0].get_text().strip() == "":
                del p[0]

            temp_chapter_name = nameSpan.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
            if temp_chapter_name == temp_chapter_name_in_body:
                print("equals")
                del p[0]
            name = nameSpan

        elif url.find('novel/martial-world/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
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
                    print("equals")
                    name = p[0]
                    del p[0]

        elif url.find('novel/ancient-strengthening-technique/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
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
                    print("equals")
                    name = p[0]
                    del p[0]

        elif url.find('novel/rmji/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 6:
                div = divUpper.find('div', {"id": "chapterContent"})
                p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")

            temp_chapter_name = temp_chapter_name.split("Chapter")
            if len(temp_chapter_name) > 1:
                del temp_chapter_name[0]
            temp_chapter_name = "Chapter".join(temp_chapter_name).strip()

            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
            if temp_chapter_name == temp_chapter_name_in_body:
                print("equals")
                name = p[0]
                del p[0]

        elif url.find('novel/stop-friendly-fire/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 10 and url.find('novel/stop-friendly-fire') != -1:
                p = div.find_all("div", recursive=MAKE_P_RECURSICE) + p

            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ")
            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
            if temp_chapter_name == temp_chapter_name_in_body:
                print("equals")
                name = p[0]
                del p[0]

        elif url.find('novel/the-charm-of-soul-pets') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            if len(p) < 6:
                p = div.find_all("p", recursive=True)

            while p[0].get_text().strip() == "":
                del p[0]
            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")

            temp_chapter_name = temp_chapter_name.split("Chapter")
            if len(temp_chapter_name) > 1:
                del temp_chapter_name[0]
            temp_chapter_name = "Chapter".join(temp_chapter_name).strip()

            temp_chapter_name_in_body = temp_chapter_name_in_body.split("Chapter")
            if len(temp_chapter_name_in_body) > 1:
                del temp_chapter_name_in_body[0]
            temp_chapter_name_in_body = "Chapter".join(temp_chapter_name_in_body).strip()

            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)

            if temp_chapter_name == temp_chapter_name_in_body:
                print("equals")
                name = p[0]
                del p[0]

        elif url.find('novel/demon-hunter/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            while p[0].get_text().strip() == "":
                del p[0]
            name = p[0]
            del p[0]

        elif url.find('novel/city-of-sin/') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            while p[0].get_text().strip() == "":
                del p[0]

        elif url.find('wuxiaworld.com') != -1:
            divSectionContent = soup.find('div', {"class": "section-content"})
            divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
            divUpper = divUpperAll[-1]
            name = divUpper.h4
            div = divUpper.find('div', {"class": "fr-view"})
            replace_ul(div, soup)
            replace_hr(div, soup)
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

            while p[0].get_text().strip() == "":
                del p[0]
            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")
            
            temp_chapter_name = temp_chapter_name.split("Chapter")
            if len(temp_chapter_name) > 1:
                del temp_chapter_name[0]
            temp_chapter_name = "Chapter".join(temp_chapter_name).strip()
            
            temp_chapter_name_in_body = temp_chapter_name_in_body.split("Chapter")
            if len(temp_chapter_name_in_body) > 1:
                del temp_chapter_name_in_body[0]
            temp_chapter_name_in_body = "Chapter".join(temp_chapter_name_in_body).strip()
            
            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)

            if temp_chapter_name == temp_chapter_name_in_body:
                print("equals")
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

        if url.find('novel/city-of-sin/') != -1:
            name = name + " - " + p[0].get_text()
            name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"')
            name = re.sub(r' [ ]+', r' ', name)
            name = re.sub(r'^0+', '', name)
            name = name.strip()
            del p[0]
        else:
            name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"').replace(u'\u3011', "]").replace(u'\u3010', "[")
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

    if HTML_SAVE_ONLY_FLAG:
        save_website(url, src, name)
        return None, None
    if SAVE_HTML_WITH_DOWNLOAD:
        save_website(url, src, name, save_path or HTML_SAVE_PATH, save_folder or HTML_FOLDER_NAME)

    # Body Extraction
    content = ""
    for i in p:
        # Webnovel Pirate tag
        if i.pirate:
            i.pirate.decompose()
        if i.sup:
            if i.sup.a:
                i.sup.a.unwrap()
            i.sup.unwrap()
        if i.strong:
            i.strong.unwrap()
        if i.em:
            replace_em(i, soup)
            i.em.unwrap()
        if i.br:
            t = i.get_text(separator="\n")
        else:
            t = i.get_text()
        # tempLower = t.lower()
        # if tempLower.find('patreon') != -1 and tempLower.find('support') != -1:
        #     break
        t = t.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"\u2013", u"-").replace(u"\xa0", u" ")
        t = re.sub(r'^\s+', r'', t)
        t = re.sub(r'\s+$', r'', t)
        t = re.sub(r"''+", r"'", t)
        # t = re.sub(r'^\s+$', r'', t)
        # t = t.strip()
        if t == "":
            continue
        content += t + "\n\n"
    content = content.strip()

    # content = re.sub(r'^(Edited|Translated)\sby\s?:\s?.*$\n*', '', content)
    # content = re.sub(r'([\w\W\s\S]*)Do you want to read up to [0-9]{1,2} unreleased chapters\? Support UTS on Patreon!', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*)Advertisement\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*)\>\s*Teaser\s*for\s*Next\s*Chapter\s*\<\Z', r'\1', content, flags=re.IGNORECASE))
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*)This\s*Chapter.?s\s*Teaser\Z', r'\1', content, flags=re.IGNORECASE))
    # content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)\[Previous\sChapter\][\s]*\[Table\sof\sContents\][\s]*\[Next\sChapter\]\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*\|[\s]*Index[\s]*\|[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    content = re.sub(r'([\w\W\s\S]*)«(\s)?Previous(\sChapter)?[\s]*\|[\s]*Next\sChapter(\s)?»\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    content = re.sub(r'([\w\W\s\S]*).Previous\s*Chapter[\s]*\|[\s]*Next\s*Chapter.?\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    content = re.sub(r'\n +\n', r'\n\n', content, flags=re.IGNORECASE)
    content = re.sub(r'\n\n[\n]+', r'\n\n', content, flags=re.IGNORECASE)
    content = content.strip()

    # Foot note Extraction
    foot = soup.find("div", {"class": "footnotes"})
    if foot:
        content = re.sub(r'\n----+\Z', r'', content, flags=re.IGNORECASE)
        content = content.strip()
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
            content = re.sub(r'\n----+\Z', r'', content, flags=re.IGNORECASE)
            content = content.strip()
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
    if name is None:
        time.sleep(1)
        return
    save_chapter(name, content, url)

def main():
    if LIST_TRUE:
        if SKIP_NAME:
            for l in LIST:
                name, content = get_content(l[0], l[1])
                if name is None:
                    time.sleep(1)
                    continue
                save_chapter(name, content, l[0])
        else:
            if len(LIST) < 3:
                for url in LIST:
                    name, content = get_content(url)
                    if name is None:
                        time.sleep(1)
                        continue
                    save_chapter(name, content, url)
                    time.sleep(1)
            else:
                with Pool(3) as pool:
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
            print(i, temp[0])
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

    if tempUrl is None:
        urls = get_urls()
    else:
        urls = [tempUrl]

    signal.signal(signal.SIGINT, signal_handler)

    if len(urls) < 3:
        for url in urls:
            name, content = get_content(url)
            if name is None:
                time.sleep(1)
                continue
            save_chapter(name, content, url)
            time.sleep(1)
    else:
        with Pool(3) as pool:
            try:
                pool.map(download_chapter, urls, chunksize=1)
            except KeyboardInterrupt:
                print("Caught KeyboardInterrupt, terminating workers")
                pool.terminate()
            else:
                print("Normal termination")
                pool.close()
            pool.join()


if __name__ == '__main__':
    main()
