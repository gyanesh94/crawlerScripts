from Exceptions.UrlInvalidStatusCode import UrlInvalidStatusCode

from bs4 import BeautifulSoup
from urllib.parse import urlparse

import requests


def print_text(s=""):
    print(s)


def print_object(o):
    print(o)


def format_text(s: str) -> str:
    return s.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"  ", u" ").replace(u"\u2013", u"-").replace(u"\xa0", u" ").strip()


def parse_html(html) -> BeautifulSoup:
    return BeautifulSoup(html, 'lxml')


def extract_text(html: BeautifulSoup) -> str:
    return format(html.text)


def episode_list_url(anime_id="", page=1) -> str:
    return f"https://animepahe.com/api?m=release&id={anime_id}&sort=episode_asc&l=30&page={page}"


def download_link_url(anime_id="", session_id="") -> str:
    return f"https://animepahe.com/api?m=links&id={anime_id}&session={session_id}&p=kwik"


def list_empty(l: list):
    return l is None or len(l) == 0


def get_src(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    UrlInvalidStatusCode(url, r.status_code)


def get_anime_url_path(url):
    url = urlparse(url)
    path = url.path.split("/")
    for index in range(len(path) - 1, -1, -1):
        if len(path[index]) > 0:
            return path[index]
