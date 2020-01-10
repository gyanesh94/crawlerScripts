# -*- coding: utf-8 -*-
import logging
from os import makedirs, path
from urllib.parse import urljoin, urlsplit

import scrapy
from scrapy.http import Request

from webnovel_scrapy.config.WuxiaWorldDownloadConfig import *
from webnovel_scrapy.extraFunctions.functionsLxml import *


def get_full_novel_path(url):
    url = urlsplit(url)
    domain = url.hostname
    novel_path = url.path[1:]
    full_path = path.join(BASE_PATH, domain, novel_path)
    if not path.exists(full_path):
        makedirs(full_path)
    return full_path


def get_novel_file_name(url):
    return f"{url.split('/')[-1]}.html"


class WuxiaWorldDownloadSpider(scrapy.Spider):
    name = "WuxiaWorldDownloadSpider"

    def __init__(self, summary_url=None, **kw):
        self.summary_url = summary_url
        self.URLS = set()
        self.full_path = None
        super(WuxiaWorldDownloadSpider, self).__init__(**kw)

    def start_requests(self):
        if self.summary_url:
            urlRequest = [Request(self.summary_url, callback=self.parse)]
            return urlRequest
        for index, novel in enumerate(NOVEL_URLS):
            print(f"{index}: {novel[NOVEL_NAME]}")
        selected_index = int(input("Input= "))
        selected_novel = NOVEL_URLS[selected_index]
        if selected_novel[CHAPTER_URL_IN_SEQUENTIAL]:
            chapter_url = selected_novel[CHAPTER_URL]
            for index in range(selected_novel[CHAPTER_START], selected_novel[CHAPTER_END] + 1):
                self.URLS.add(chapter_url.format(index))
        urlRequest = [Request(selected_novel[SUMMARY_URL], callback=self.parse)]
        return urlRequest

    def parse(self, response):
        if response.status != 200:
            logger.warning(f"Failed to fetch URL: {response.url}")
            return
        self.full_path = get_full_novel_path(response.url)

        with open(path.join(self.full_path, "0_summary.html"), 'wb') as chapter_file:
            chapter_file.write(response.body)

        parsed_content = parseHtml(response.body)
        chapter_paths_array = parsed_content.xpath(SUMMARY_PAGE_A_LINK_XPATH)
        if chapter_paths_array is None or not chapter_paths_array:
            return None
        for a_link in chapter_paths_array:
            href = a_link.get('href').strip()
            if href is None or not href:
                continue
            self.URLS.add(urljoin(response.url, href))
        urlRequest = [Request(url, callback=self.parse_novel_chapter) for url in self.URLS]
        return urlRequest

    def parse_novel_chapter(self, response):
        if response.status != 200:
            logger.warning(f"Failed to fetch URL: {response.url}")
            return
        with open(path.join(self.full_path, get_novel_file_name(response.url)), 'wb') as chapter_file:
            chapter_file.write(response.body)
