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
import requests
import cfscrape

MAKE_P_RECURSICE = False

url_list = [
    ["atg", "http://www.wuxiaworld.com/atg-index/atg-chapter-{}/"],
    ["csg", "http://gravitytales.com/chaotic-sword-god/csg-chapter-{}/"],
    ["col", "http://www.wuxiaworld.com/col-index/col-volume-9-chapter-{}/"],
    ["hjc", "http://www.wuxiaworld.com/hjc-index/hjc-chapter-48-{}/"],
    ["issth", "http://www.wuxiaworld.com/issth-index/issth-book-4-chapter-{}/"],
    ["mga", "https://www.wuxiaworld.com/novel/martial-god-asura/mga-chapter-{}/"],
    ["tdg", "http://www.wuxiaworld.com/tdg-index/tdg-chapter-{}/"],
    ["de", "http://www.wuxiaworld.com/desolate-era-index/de-book-12-chapter-{}/"],
    ["pw", "http://www.wuxiaworld.com/pw-index/pw-chapter-{}/"],
    ["tgr", "http://www.wuxiaworld.com/tgr-index/tgr-chapter-{}/"],
    ["wdqk", "http://www.wuxiaworld.com/wdqk-index/wdqk-chapter-{}/"],
    ["tmw", "http://gravitytales.com/true-martial-world/tmw-chapter-{}/"],
    ["God and devil", "http://www.translationnations.com/translations/god-and-devil-world/god-and-devil-world-chapter-0{}/"]
]


def get_url():
    parser = argparse.ArgumentParser(description='Fetch Url')
    parser.add_argument('-u', action="store", default=None, dest='url', help="give url")
    url = parser.parse_args().url
    return url


def get_src(url):
    r = requests.get(url)
    if r.status_code == 503:
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
        path = "/Users/gyanesh/Dropbox/Web Novels/Web Novel alias/New Updates/"
        # path = "/Users/gyanesh/Documents/.a/Web Novel alias/"
        # path = "/Users/gyanesh/Google Drive/Web Novels/Web Novel alias/"
        # path = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/"
    name = path + name
    text = open(name + ".txt", "w")
    text.write(content)
    text.close()


def replace_ul(elem, soup):
    return
    ul_s = elem.find_all("ul", recursive=MAKE_P_RECURSICE)
    for ul in ul_s:
        new_elem = soup.new_tag("p")
        text = ""
        li_s = ul.find_all("li", recursive=MAKE_P_RECURSICE)
        for li in li_s:
            t = li.get_text()
            text = "{}- {}\n".format(text, li.get_text())
        text = text.strip()
        new_elem.string = text
        elem.ul.replace_with(new_elem)
        # print(ul)


def get_content(url):
    src = get_src(url)
    p = []
    soup = BeautifulSoup(src, 'lxml')
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
    if url.find('novelfull.com/') != -1:
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
            print "equals"
            del p[0]
        name = nameSpan

    elif url.find('novel/martial-world/') != -1:
        divSectionContent = soup.find('div', {"class": "section-content"})
        divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
        divUpper = divUpperAll[-1]
        name = divUpper.h4
        div = divUpper.find('div', {"class": "fr-view"})
        replace_ul(div, soup)
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
        replace_ul(div, soup)
        p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if len(p) < 6:
            div = divUpper.find('div', {"id": "chapterContent"})
            p = div.find_all("p", recursive=MAKE_P_RECURSICE)

        if re.findall('(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()) != []:
            print(re.findall('(?:AST|Chapter).*(?:\s|-|^)[0-9]{1,5}(?:\s|-)', p[0].get_text()))
            name = p[0]
            del p[0]
        else:
            temp_chapter_name = name.get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")
            temp_chapter_name_in_body = p[0].get_text().strip().replace(u'\u2019', '').replace("'", '').replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"-", u" ").replace(u",", u"").replace(u":", u"")
            temp_chapter_name = re.sub(r' [ ]+', r' ', temp_chapter_name, flags=re.IGNORECASE)
            temp_chapter_name_in_body = re.sub(r' [ ]+', r' ', temp_chapter_name_in_body, flags=re.IGNORECASE)
            if temp_chapter_name == temp_chapter_name_in_body:
                print "equals"
                name = p[0]
                del p[0]

    elif url.find('novel/rmji/') != -1:
        divSectionContent = soup.find('div', {"class": "section-content"})
        divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
        divUpper = divUpperAll[-1]
        name = divUpper.h4
        div = divUpper.find('div', {"class": "fr-view"})
        replace_ul(div, soup)
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
            print "equals"
            name = p[0]
            del p[0]

    elif url.find('novel/stop-friendly-fire/') != -1:
        divSectionContent = soup.find('div', {"class": "section-content"})
        divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
        divUpper = divUpperAll[-1]
        name = divUpper.h4
        div = divUpper.find('div', {"class": "fr-view"})
        replace_ul(div, soup)
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

    elif url.find('novel/the-charm-of-soul-pets') != -1:
        divSectionContent = soup.find('div', {"class": "section-content"})
        divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
        divUpper = divUpperAll[-1]
        name = divUpper.h4
        div = divUpper.find('div', {"class": "fr-view"})
        replace_ul(div, soup)
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
            print "equals"
            name = p[0]
            del p[0]

    elif url.find('novel/city-of-sin/') != -1:
        divSectionContent = soup.find('div', {"class": "section-content"})
        divUpperAll = divSectionContent.find_all('div', {"class": "panel-default"})
        divUpper = divUpperAll[-1]
        name = divUpper.h4
        div = divUpper.find('div', {"class": "fr-view"})
        replace_ul(div, soup)
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

    if url.find('novel/city-of-sin/') != -1:
        name = name + " - " + p[0].get_text()
        name = name.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"')
        name = re.sub(r' [ ]+', r' ', name)
        name = re.sub(r'^0+', '', name)
        name = name.strip()
        del p[0]
    else:
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

# urls = get_urls()

urls = [raw_input()]

for url in urls:
    name, content = get_content(url)
    save_chapter(name, content, url)
