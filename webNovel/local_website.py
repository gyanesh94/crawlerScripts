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

from bs4 import BeautifulSoup, NavigableString
import argparse
import re
import signal
import os
import time
from listings_download import *
from multiprocessing import Pool

SKIP_DEFAULT = True
MAKE_P_RECURSICE = False

NAME_FROM_HTML = False

if LIST_TRUE or SKIP_DEFAULT:
    SAVE_DIRECTORY = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/"
else:
    SAVE_DIRECTORY = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/"

TEMP_DIRECTORY = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/"
LOCAL_WEBSITE = True

FILE_NAMES = [
]

if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

def print_html(html):
    print(html.prettify())


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

    elif url.find("/novel/overgeared/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Overgeared/"
        """
        og-chapter-335      # numbering
        og-chapter-355
        og-chapter-748
        og-chapter-806
        """

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

    elif url.find("/novel/trash-of-the-counts-family/") != -1:
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/Ongoing/Trash of the Count's Family/"

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

    if LOCAL_WEBSITE:
        if not os.path.exists(TEMP_DIRECTORY):
            os.makedirs(TEMP_DIRECTORY)
        path = TEMP_DIRECTORY

    name = os.path.join(path, name)
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


def get_content(url, content, getName=""):
    print(url)
    # src = get_src(url)
    soup = BeautifulSoup(content, 'lxml')
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

    elif url.find('readlightnovel.') != -1:
        div_header = soup.find('div', {"class": "section-header-title"})
        nameSpan = div_header.find('span')
        if not nameSpan:
            print(f"nameSpan for {url} not found")
            return

        div = soup.find("div", {"id": "chapterText"})
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

        if temp_chapter_name.startswith("chapter "):
            name = p[0]
            del p[0]
        else:
            name = nameSpan

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

    elif url.find('readnovelfull.com/') != -1:
        div = soup.find('div', {"class": "cha-content"})
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
            temp_outer_text = p[0].parent.find(text=True, recursive=False)
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
            temp_outer_text = p[0].parent.find(text=True, recursive=False)
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

        if re.findall('(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()) != []:
            print(re.findall('(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()))
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
    # content = re.sub(r'([\w\W\s\S]*)Previous(\sChapter)?[\s]*Next\sChapter\Z', r'\1', content, flags=re.IGNORECASE)
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
    save_chapter(name, content, url)


def convert_local_html_to_txt():
    # d = "/Users/gyanesh/Documents/Web Novels/websites/comrademao.com/Long Live Summons/701-800/"
    # url = "https://comrademao.com/"
    # d = "/Users/gyanesh/Documents/Web Novels/websites/www.centinni.com/Long Live Summons/761-798/"
    # url = "https://www.centinni.com/"
    # d = "/Users/gyanesh/Documents/Web Novels/websites/novelfull.com/The World after the Fall/"
    # url = "https://novelfull.com/"
    d = "/Users/gyanesh/Documents/Web Novels/websites/www.wuxiaworld.com/novel/the-regressed-demon-lord-is-kind/"
    url = "wuxiaworld.com"
    d = "/Users/gyanesh/Documents/Web Novels/websites/rainingtl.org/Kidnapped Dragons/"
    url = "rainingtl.org"
    # d = "/Users/gyanesh/Documents/Web Novels/websites/mostnovel.com/Sealed Divine Throne/"
    # url = "mostnovel.com/"
    print(f"Start: {FILE_NAMES[0]}\tEnd: {FILE_NAMES[-1]}")
    print("--------------------------------")
    for i in FILE_NAMES:
        with open(os.path.join(d, i), 'rb') as story_summary_file:
            content = story_summary_file.read()
            name, content = get_content(url, content)
            if NAME_FROM_HTML:
                name = i.replace(".html", "")
            save_chapter(name, content, url)

    # for i in range(1232, 1245):
    #     with open(os.path.join(d, f'og-chapter-{i}.html'), 'rb') as story_summary_file:
    #         content = story_summary_file.read()
    #         name, content = get_content(url, content)
    #         save_chapter(name, content, url)


# if LIST_TRUE:
#     if SKIP_NAME:
#         for l in LIST:
#             name, content = get_content(l[0], l[1])
#             save_chapter(name, content, l[0])
#     else:
#         if len(LIST) < 3:
#             for url in LIST:
#                 name, content = get_content(url)
#                 save_chapter(name, content, url)
#                 time.sleep(1)
#         else:
#             pool = Pool(3)
#             try:
#                 pool.map(download_chapter, LIST, chunksize=1)
#             except KeyboardInterrupt:
#                 print("Caught KeyboardInterrupt, terminating workers")
#                 pool.terminate()
#             else:
#                 print("Normal termination")
#                 pool.close()
#             pool.join()
#     exit()


# def get_urls():
#     i = 0
#     for temp in url_list:
#         print(i, temp[0])
#         i = i + 1
#     url = url_list[input("Index= ")][1]
#     start = input("Start= ")
#     end = raw_input("End= ")
#     if end == "":
#         end = start
#     else:
#         end = int(end)
#     l = []
#     for i in range(start, end + 1):
#         l += [url.format(i)]
#     return l


# tempUrl = get_url()

# if LIST is not None and LIST != []:
#     urls = LIST
# elif tempUrl is None:
#     urls = get_urls()
# else:
#     urls = [tempUrl]

# signal.signal(signal.SIGINT, signal_handler)

# if len(urls) < 3:
#     for url in urls:
#         name, content = get_content(url)
#         save_chapter(name, content, url)
#         time.sleep(1)
# else:
#     pool = Pool(3)
#     try:
#         pool.map(download_chapter, urls, chunksize=1)
#     except KeyboardInterrupt:
#         print("Caught KeyboardInterrupt, terminating workers")
#         pool.terminate()
#     else:
#         print("Normal termination")
#         pool.close()
#     pool.join()


if __name__ == '__main__':
    convert_local_html_to_txt()
