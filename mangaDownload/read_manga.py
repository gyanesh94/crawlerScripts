#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import os
import sys
import signal
import getopt


def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        exit()


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


def url_encode(url):
    url = url.strip()
    url = url.encode(encoding='unicode_escape')
    url = url.replace("\u2018", "'").replace("\u2019", "'")
    return url


def str_encode(name):
    name = name.strip()
    name = name.replace(':', '-')
    name = name.encode(encoding='unicode_escape')
    name = name.replace("\u2018", "'").replace("\u2019", "'")
    return name


def get_chapters(chapters, url):
    links = []
    for chapter in chapters:
        href = chapter.a['href'] + "/all-pages"
        href = url_encode(href)
        name = chapter.span.contents[1]
        name = str_encode(name)
        links.append([href, name])
    return links


def get_image_links(url):
    src = get_src(url)
    soup = BeautifulSoup(src, 'html.parser')
    div = soup.find_all("div", {"class": "page_chapter"})
    for t in div:
        image = t.find("img")
        if image is not None:
            break
    pages = []
    while image:
        href = image["src"]
        name = href.split("/")[-1]
        href = url_encode(href)
        name = str_encode(name)
        extension = name.split(".")[-1]
        extension = extension.split("?")[0]
        pages.append([href, extension])
        image = image.img
    return pages


def get_images(href, name):
    pages = get_image_links(href)
    name = name.replace(".", "_")
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)
    i = 0
    for page in pages:
        tmpName = "{name} Page {index:03}.{ext}".format(name=name, index=i, ext=page[1])
        tmpName = tmpName.replace("-", " ").replace("  ", " ").replace("  ", " ")
        axel = 'axel -aqo "' + tmpName + '" ' + page[0]
        i = i + 1
        os.system(axel)
        # urllib.urlretrieve(page[0],page[1])
    os.chdir("..")

signal.signal(signal.SIGINT, signal_handler)

url = get_url()

if url:
    src = get_src(url)
    soup = BeautifulSoup(src, 'html.parser')
    ul = soup.find("ul", {"class": "chp_lst"})
    chapters = get_chapters(ul.find_all("li"), url)
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
                for i in range(int(choices[1]), int(choices[2]) + 1):
                    chapter = chapters[i]
                    get_images(chapter[0], chapter[1])
            else:
                choices = filter(lambda x: x.isdigit(), choices)
                if choices:
                    choices = map(lambda x: int(x), choices)
                    for choice in choices:
                        chapter = chapters[choice]
                        get_images(chapter[0], chapter[1])
