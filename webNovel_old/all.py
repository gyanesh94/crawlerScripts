# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
1. Against The God
2. Skyfire Avenue
3. Martial God Asura
4. The Great Ruler
5. Tales of Demons And Gods
6. Coiling Dragon
7. I Shall Seal the Heavens
8. Chaotic God Sword (Beware Of Comments)
8. Desolate Era
9. Stellar Transformations
"""

from bs4 import BeautifulSoup, NavigableString
import argparse
import re
import signal
import os
import requests
import cfscrape
import time
import cloudscraper
from listings_download import *
from multiprocessing import Pool
from urllib.parse import urlsplit
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SKIP_DEFAULT = False
MAKE_P_RECURSICE = False

sessions = requests.session()
sessions.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
scraper = cloudscraper.create_scraper()

if USE_SELENIUM:
    # dr = webdriver.Chrome("/Users/gyanesh/bin/chromedriver")
    firefox_options = Options()
    firefox_options.set_preference("browser.link.open_newwindow.restriction", 0)
    firefox_options.set_preference("browser.link.open_newwindow", 3)
    dr = webdriver.Firefox(options = firefox_options)

if LIST_TRUE or SKIP_DEFAULT:
    SAVE_DIRECTORY = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/"
else:
    SAVE_DIRECTORY = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/"

if not LIST and TO_BE_FORMAT_URL is not None:
    for i in range(START_PAGE, END_PAGE + 1):
        LIST.append(TO_BE_FORMAT_URL.format(i))

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
    s = scraper.get(url)
    s.encoding = 'utf-8'
    return s.text
    # r = requests.get(url, headers=headers)
    # if r.status_code == 503 or r.status_code == 403:
    #     print("test")
    #     # scraper = cfscrape.create_scraper()
    # elif r.status_code == 200:
    #     r.encoding = 'utf-8'
    #     return r.text
    # exit()


def save_website(url, txt, name, save_path=HTML_SAVE_PATH, save_folder=HTML_FOLDER_NAME):
    url = urlsplit(url)
    domain = url.hostname
    if (domain.endswith(".app")):
        domain = domain.replace(".app", "_app")
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
    name = name.encode(encoding='unicode_escape')
    name = name.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", '--')
    name = name.replace(':', '-').replace('- -', '-')
    name = name.replace('"', "'")
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

def wrap_text_without_tag_with_p(elem, soup):
    while True:
        inner_text_without_tag = elem.find(string=True, recursive=False)
        if not inner_text_without_tag:
            return
        new_elem = soup.new_tag("p")
        new_elem.string = inner_text_without_tag.get_text().strip()
        inner_text_without_tag.replace_with(new_elem)

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


def expand_li_ul(elem, soup):
    ul_s = elem.find_all("ul", recursive=MAKE_P_RECURSICE)
    ol_s = elem.find_all("ol", recursive=MAKE_P_RECURSICE)
    li_s = elem.find_all("li", recursive=MAKE_P_RECURSICE)

    queue = ul_s + ol_s + li_s

    while queue:
        pop_elem = queue.pop(0)
        child_ul_s = pop_elem.find_all("ul", recursive=MAKE_P_RECURSICE)
        child_ol_s = pop_elem.find_all("ol", recursive=MAKE_P_RECURSICE)
        child_li_s = pop_elem.find_all("li", recursive=MAKE_P_RECURSICE)

        if not child_ul_s and not child_ol_s and not child_li_s:
            if not pop_elem.p:
                pop_elem.string = f"- {pop_elem.string}"
                pop_elem.string.wrap(soup.new_tag("p"))
        wrap_text_without_tag_with_p(pop_elem, soup)
        if child_ul_s:
            queue.extend(child_ul_s)
        if child_ol_s:
            queue.extend(child_ol_s)
        if child_li_s:
            queue.extend(child_li_s)

        pop_elem.unwrap()

def get_content(url, getName=""):
    print(url)
    if USE_SELENIUM:
        dr.get(url)
        time.sleep(3)
        soup = BeautifulSoup(dr.page_source, "lxml")
        src = soup.prettify()
    else:
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
        name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', "'").replace(u'\u201C', "'").replace(u'\u3011', "]").replace(u'\u3010', "[").replace(u'- -', '-').replace(u'"', "'")
        name = re.sub(r' [ ]+', r' ', name)
        name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^0', '', name, flags=re.IGNORECASE)
        skipped_name = name.strip()

    if url.find('daonovel.com/') != -1:
        div_header = soup.find('div', {"class": "cha-tit"})
        header = None
        if not div_header:
            div_header = soup.find('div', {"class": "bookname"})
            header = div_header.find('h1')
        else:
            header = div_header.find('h3')
        if not header:
            print("daonovel.com header not found")
            exit()

        # div_entry_content = soup.find("div", {"class": "cha-content"})
        # div = div_entry_content.find("div", {"class": "cha-words"})
        # p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        # if len(p) < 8:
        #     p = div.find_all("p", recursive=True)
        # while p[0].get_text().strip() == "":
        #     del p[0]

        name = header

    elif url.find('rainingtl.org') != -1:
        h1_header = soup.find('h1', {"class": "entry-title"})
        if not h1_header:
            print("rainingtl name not found")
            exit()

        div = soup.find("div", {"class": "entry-content"})
        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        name = h1_header

    elif url.find('divinedaolibrary.com/') != -1:
        h1_header = soup.find('h1', {"class": "entry-title"})
        if not h1_header:
            print("divinedaolibrary name not found")
            exit()

        div = soup.find("div", {"class": "entry-content"})
        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        name = h1_header

    elif url.find('www.centinni.com/') != -1:
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

    elif url.find('readlightnovel.') != -1 or url.find('readln.org') != -1 or url.find('rln.app') != -1:
        div_header = soup.find('div', {"class": "section-header-title"})
        nameSpan = div_header.find('span')
        if not nameSpan:
            print(f"nameSpan for {url} not found")
            return

        div = soup.find("div", {"id": "chapterText"})
        wrap_text_without_tag_with_p(div, soup)
        for elem in div.find_all(["center", "pirate"]):
            elem.decompose()
        for elem in div.find_all(["hr"]):
            new_elem = soup.new_tag("p")
            new_elem.string = "-------"
            elem.replace_with(new_elem)
        for elem in div.find_all(["ul"]):
            new_elem = soup.new_tag("p")
            text = ""
            li_s = elem.find_all("li", recursive=MAKE_P_RECURSICE)
            for li in li_s:
                text = f"{text}- {li.get_text()}\n"
            text = text.strip()
            new_elem.string = text
            elem.replace_with(new_elem)
        for elem in div.find_all(["sup", "a", "strong"]):
            elem.unwrap()
        for elem in div.find_all(["em"]):
            emtext = elem.get_text().replace(u'\u2060', ' ').replace(u'\xc2\xa0', ' ').replace(u'\xa0', ' ')
            if len(emtext):
                if emtext[-1] == " ":
                    elem.string = f"'{emtext[:-1]}' "
                else:
                    elem.string = f"'{emtext}'"
            elem.unwrap()
        for elem in div.find_all(["p", "div", "h3"]):
            if elem.get_text().strip() == "SPONSORED CONTENT":
                elem.decompose()
                continue
            elem.replace_with(elem.text + "\n\n")
        for elem in div.find_all(["br"]):
            elem.replace_with("\n\n")

        test_list = div.get_text().split("\n")
        p = list(filter(lambda x: len(x.strip()) > 0, test_list))

        temp_chapter_name = p[0].strip().lower().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")

        if temp_chapter_name.startswith("chapter ") or url.find("-circle-of-inevitability") != -1:
            name = p[0]
            del p[0]
        else:
            name = nameSpan

    elif url.find('skydemonorder.com') != -1:
        header = soup.find('header')
        div_h1 = header.find('h1')
        if not div_h1:
            print(f"div_h1 for {url} not found")
            return

        div = soup.find("div", {"class": "prose"})
        wrap_text_without_tag_with_p(div, soup)
        for elem in div.find_all(["center", "pirate"]):
            elem.decompose()
        for elem in div.find_all(["hr"]):
            new_elem = soup.new_tag("p")
            new_elem.string = "-------"
            elem.replace_with(new_elem)
        for elem in div.find_all(["ul"]):
            new_elem = soup.new_tag("p")
            text = ""
            li_s = elem.find_all("li", recursive=MAKE_P_RECURSICE)
            for li in li_s:
                text = f"{text}- {li.get_text()}\n"
            text = text.strip()
            new_elem.string = text
            elem.replace_with(new_elem)
        for elem in div.find_all(["sup", "a", "strong"]):
            elem.unwrap()
        for elem in div.find_all(["em"]):
            emtext = elem.get_text().replace(u'\u2060', ' ').replace(u'\xc2\xa0', ' ').replace(u'\xa0', ' ')
            if len(emtext):
                if emtext[-1] == " ":
                    elem.string = f"'{emtext[:-1]}' "
                else:
                    elem.string = f"'{emtext}'"
            elem.unwrap()
        for elem in div.find_all(["p", "div", "h3"]):
            if elem.get_text().strip() == "SPONSORED CONTENT":
                elem.decompose()
                continue
            elem.replace_with(elem.text + "\n\n")
        for elem in div.find_all(["br"]):
            elem.replace_with("\n\n")

        test_list = div.get_text().split("\n")
        p = list(filter(lambda x: len(x.strip()) > 0, test_list))

        name = div_h1

    elif url.find('mostnovel.com/') != -1:
        div_header = soup.find('div', {"class": "entry-header"})
        option = div_header.find('option', {"selected": "selected"})
        if not option:
            print("mostnovel name not found")
            exit()

        div_entry_content = soup.find("div", {"class": "entry-content"})
        div = div_entry_content.find("div", {"class": "text-left"})
        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        name = option

    elif url.find('eatapplepies.com') != -1:
        h1 = soup.find('h1', {"class": "entry-title"})
        if not h1:
            exit()

        div = soup.find("div", {"class": "entry-content"})
        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        name = h1

    elif url.find('lightnovelcave.com') != -1:
        h1 = soup.find('span', {"class": "chapter-title"})
        if not h1:
            exit()

        div = soup.find("div", {"id": "chapter-container"})
        wrap_text_without_tag_with_p(div, soup)
        expand_li_ul(div, soup)
        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        name = h1

    elif url.find('wangmamaread.com') != -1:
        h3 = soup.find('h3', {"class": "entry-title"})
        if not h3:
            exit()

        div = soup.find("div", {"class": "entry-content"})
        wrap_text_without_tag_with_p(div, soup)
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
        wrap_text_without_tag_with_p(div, soup)

        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        name = p[0]
        del p[0]

    elif url.find('readnovelfull.com/') != -1:
        div = soup.find('div', {"class": "cha-content"})
        wrap_text_without_tag_with_p(div, soup)
        nameSpan = soup.find('div', {"class": "cha-tit"})

        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        temp_chapter_name = nameSpan.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
        temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
        temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
        temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
        if temp_chapter_name == temp_chapter_name_in_body:
            print("equals")
            del p[0]
        else:
            temp_outer_text = p[0].parent.find(string=True, recursive=False)
            if temp_outer_text:
                temp_outer_text = temp_outer_text.strip()

            if temp_outer_text and temp_outer_text.find("full thich ung") == -1:
                html_temp = "<p></p>"
                soup_temp = BeautifulSoup(html_temp, 'lxml')
                ptag_temp = soup.find('p')
                ptag_temp.insert(0, NavigableString(temp_outer_text))
                p.insert(0, ptag_temp)
        name = nameSpan

    elif url.find('novelfull.com/') != -1:
        div = soup.find('div', {"id": "chapter-content"})
        wrap_text_without_tag_with_p(div, soup)
        nameSpan = ""
        if url.find('swallowed-star') != -1:
            temp_div_chapter_name = soup.find('div', {"class": "breadcrumb-container"})
            temp_li_active = temp_div_chapter_name.find('li', {"class": "active"})
            nameSpan = temp_li_active.find("span")
        else:
            nameSpan = soup.find('span', {"class": "chapter-text"})

        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 8:
            p = div.find_all("p", recursive=True)
        while p[0].get_text().strip() == "":
            del p[0]

        temp_chapter_name = nameSpan.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
        temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
        temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
        temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
        if temp_chapter_name == temp_chapter_name_in_body:
            print("equals")
            del p[0]
        else:
            temp_outer_text = p[0].parent.find(string=True, recursive=False)
            if temp_outer_text:
                temp_outer_text = temp_outer_text.strip()

            if temp_outer_text and temp_outer_text.find("full thich ung") == -1:
                html_temp = "<p></p>"
                soup_temp = BeautifulSoup(html_temp, 'lxml')
                ptag_temp = soup.find('p')
                ptag_temp.insert(0, NavigableString(temp_outer_text))
                p.insert(0, ptag_temp)
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
            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
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

        if re.findall(r'(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()) != []:
            print(re.findall(r'(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()))
            name = p[0]
            del p[0]
        else:
            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
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

        temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(").replace(u",", u"").replace(u":", u"")
        temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(").replace(u",", u"").replace(u":", u"")

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

        temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
        temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(")
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
        temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(").replace(u",", u"").replace(u":", u"")
        temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(").replace(u",", u"").replace(u":", u"")

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
        temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(").replace(u",", u"").replace(u":", u"")
        temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u"\uFF09", ")").replace(u"\uFF08", "(").replace(u",", u"").replace(u":", u"")

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

    if SKIP_NAME and LIST_TRUE:
        name = skipped_name

    if not isinstance(name, str):
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
        name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', "'").replace(u'\u201C', "'").replace(u'\u3011', "]").replace(u'\u3010', "[").replace(u'- -', '-').replace(u'"', "'")
        name = re.sub(r' [ ]+', r' ', name)
        while not name or name == " " or name == "":
            name = p[0]
            del p[0]
            if not isinstance(name, str):
                name = name.get_text()
            name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', "'").replace(u'\u201C', "'").replace(u'\u3011', "]").replace(u'\u3010', "[").replace(u'- -', '-').replace(u'"', "'")
            name = re.sub(r' [ ]+', r' ', name)
        name = re.sub(r':', '-', name)
        if url.find('novel/stop-friendly-fire') != -1:
            name = name.replace(">", "").replace("<", "")
        if not dont_strip(url):
            name = name.split("Chapter")
            if len(name) > 1:
                del name[0]
            name = "Chapter".join(name)
            # name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name, 1)
            name = re.sub(r'^AST ([0-9]{1,5})', r'\1', name)
        name = re.sub(r'^0+', '', name)
        name = name.strip()
        print(name)
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
        if isinstance(i, str):
            t = i
        else:
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
    # content = re.sub(r'([\w\W\s(?# \S]*)<<Previous(\sChapter)?[\s]*\|[\s]*Index[\s]*\|[\s]*Next\sChapter>>\Z', r'\1', content, flags=re.IGNORECASE)
    # content = re.sub(r'([\w\W\s)\S]*)Previous(\sChapter)?[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*)\[Previous\sChapter\][\s]*\[Table\sof\sContents\][\s]*\[Next\sChapter\]\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*\|[\s]*Index[\s]*\|[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*)«(\s)?Previous(\sChapter)?[\s]*\|[\s]*Next\sChapter(\s)?»\Z', r'\1', content, flags=re.IGNORECASE)
    # content = content.strip()
    # content = re.sub(r'([\w\W\s\S]*).Previous\s*Chapter[\s]*\|[\s]*Next\s*Chapter.?\Z', r'\1', content, flags=re.IGNORECASE)
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
    else:
        index_foot = 1
        foot = soup.find("div", {"id": f"ftn{index_foot}"})
        foot_content = ""
        if foot:
            content = re.sub(r'\n----+\Z', r'', content, flags=re.IGNORECASE)
            content = content.strip()
            content += "\n\n" + "-----------" + "\n"
        while foot:
            lis = foot.find_all("p")
            for i in lis:
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
                foot_content += t + "\n\n"
            index_foot += 1
            foot = soup.find("div", {"id": f"ftn{index_foot}"})
        foot_content = foot_content.strip()
        content += foot_content

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
            for l in zip(LIST, NAME_LIST):
                name, content = get_content(l[0], l[1])
                if name is None:
                    time.sleep(1)
                    continue
                save_chapter(name, content, l[0])
        else:
            if len(LIST) < 3 or USE_SELENIUM or SKIP_MULTI_THREADED:
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

    if len(urls) < 3 or USE_SELENIUM or SKIP_MULTI_THREADED:
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
