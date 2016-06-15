#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import urllib
import os
import sys
import getopt


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


def get_src(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    return opener.open(url)


def str_encode(name):
    name = name.strip()
    name = name.replace(':', '-')
    name = name.encode(encoding='unicode_escape')
    name = name.replace("\u2018", "'").replace("\u2019", "'")
    return name


def url_encode(url):
    url = url.strip()
    url = url.encode(encoding='unicode_escape')
    url = url.replace("\u2018", "'").replace("\u2019", "'")
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


def get_image_links(url):
    src = get_src(url)
    soup = BeautifulSoup(src, 'html.parser')
    div = soup.find("div", {"class": "page_select"})
    options = div.find_all("option")
    pages = []
    for option in options:
        href = option["value"]
        src = get_src(href)
        soup = BeautifulSoup(src, 'html.parser')
        image = soup.find(id="image")
        href = image["src"]
        name = image["alt"] + ".jpg"
        href = url_encode(href)
        name = str_encode(name)
        pages.append([href, name])
    return pages


def get_images(href, name):
    pages = get_image_links(href)
    os.mkdir(name)
    os.chdir(name)
    for page in pages:
        urllib.urlretrieve(page[0], page[1])
    os.chdir("..")


url = get_url()

if url:
    src = get_src(url)
    soup = BeautifulSoup(src, 'html.parser')
    ch_ul = soup.find('ul', {"class": "chapter_list"})
    chapters = get_chapters(ch_ul.find_all('a'))
    if chapters:
        i = len(chapters) - 1
        for ch in reversed(chapters):
            print i, ch[1]
            i -= 1
        choices = raw_input().split()
        if choices:
            ch = choices[0]
            if ch == "a" or ch == "A":
                for chapter in reversed(chapters):
                    get_images(chapter[0], chapter[1])
            elif ch == "r" or ch == "R":
                for i in range(int(choices[2]), int(choices[1]) - 1, -1):
                    chapter = chapters[i]
                    get_images(chapter[0], chapter[1])
            else:
                choices = filter(lambda x: x.isdigit(), choices)
                if choices:
                    choices = map(lambda x: int(x), choices)
                    for choice in choices:
                        chapter = chapters[choice]
                        get_images(chapter[0], chapter[1])
