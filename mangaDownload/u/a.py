#!/Users/gyanesh/miniconda2/bin/python

from bs4 import BeautifulSoup
# import urllib2
import logging
import requests
import os
import signal
import argparse
import cfscrape
import subprocess
from imgToPdf import *
from time import sleep

LOGGING_FILE_NAME = "error.log"
LOGGING_MESSAGE_FORMAT = "%(asctime)s %(levelname)-8s %(message)s"
LOGGING_DATE_FORMAT = "%m/%d/%Y %I:%M %p"

logging.basicConfig(filename=LOGGING_FILE_NAME, format=LOGGING_MESSAGE_FORMAT, datefmt=LOGGING_DATE_FORMAT, level=logging.DEBUG)

mainDir = "/Users/gyanesh/Documents/Anime Manga/Unread"

url = "https://www.funmanga.com"
cookie_arg, user_agent = cfscrape.get_cookie_string(url)

def argumentParser():
    parser = argparse.ArgumentParser(description='Fetch Url')
    parser.add_argument('-u', action="store", default=False, dest='url', help="url")
    parser.add_argument('-p', action="store", default=False, dest='pdf', help="convert to pdf")
    parser.add_argument('-c', action="store", default=None, dest='convert', help="donot convert")
    url = parser.parse_args().url
    pdf = parser.parse_args().pdf
    convert = parser.parse_args().convert
    return url, pdf, convert


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    exit()


def get_src(url):
    # opener = urllib2.build_opener()
    # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # return opener.open(url)
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
    images = soup.find_all("img", {"class": "img-responsive"})
    # div = div[1]
    # for t in div:
    #     print t
    #     print "wqeqweq"
    #     image = t.find("img")
    #     # if image is not None:
    #     #     break
    pages = []
    for image in images:
        href = image["src"]
        name = href.split("/")[-1]
        href = url_encode(href)
        name = str_encode(name)
        extension = name.split(".")[-1]
        extension = extension.split("?")[0]
        pages.append([href, extension])
        image = image.img
    return pages


def get_images(href, name, pdf, convert, choice=None):
    pages = get_image_links(href)
    name = name.replace(".", "_").replace("'", "")
    if not os.path.isdir(name):
        os.mkdir(name)
    os.chdir(name)
    i = 0
    print(name)
    for page in pages:
        tmpName = "{name} Page {index:03}.{ext}".format(name=name, index=i, ext=page[1])
        tmpName = tmpName.replace("-", " ").replace("  ", " ").replace("  ", " ")
        axel = 'axel -ao "{name}" "{page_url}"'.format(name=tmpName, page_url=page[0])
        i = i + 1
        # os.system(axel)
        cmd = "curl --cookie '{cookie_arg}' -A '{user_agent}' -s '{url}' > '{name}'".format(cookie_arg=cookie_arg, user_agent=user_agent, url=page[0], name=tmpName)
        print(cmd)
        # subprocess.call(cmd)
        subprocess.call(["curl", "--cookie", cookie_arg, "-A", user_agent, "-s", "-o", tmpName, page[0]])
        sleep(1)
        # urllib.urlretrieve(page[0],page[1])
    os.chdir("..")
    if convert is not None:
        pass
    elif choice == 'a' or choice == 'A':
        pass
    elif pdf:
        print("test")
        convertToPdf("./" + name)
    else:
        zipCmd = "zip '{name}'.cbz -r '{name}'".format(name=name)
        print(zipCmd)
        os.system(zipCmd)

signal.signal(signal.SIGINT, signal_handler)

url, pdf, convert = argumentParser()

os.chdir(mainDir)

if url:
    src = get_src(url)
    soup = BeautifulSoup(src, 'html.parser')
    ul = soup.find("ul", {"class": "chp_lst"})
    chapters = get_chapters(ul.find_all("li"), url)
    if chapters:
        i = len(chapters) - 1
        for ch in reversed(chapters):
            print(i, ch[1])
            i -= 1
        choices = raw_input().split()
        if choices:
            ch = choices[0]
            if ch == "a" or ch == "A":
                comicName = url.split("/")[-1]
                if not os.path.isdir(comicName):
                    os.mkdir(comicName)
                os.chdir(comicName)
                for chapter in reversed(chapters):
                    get_images(chapter[0], chapter[1], pdf, convert, ch)
            elif ch == "r" or ch == "R":
                for i in range(int(choices[1]), int(choices[2]) + 1):
                    chapter = chapters[i]
                    get_images(chapter[0], chapter[1], pdf, convert)
            else:
                choices = filter(lambda x: x.isdigit(), choices)
                if choices:
                    choices = map(lambda x: int(x), choices)
                    for choice in choices:
                        chapter = chapters[choice]
                        # print(chapter)
                        get_images(chapter[0], chapter[1], pdf, convert)
