# -*- coding: utf-8 -*-
import logging
from collections import defaultdict
from os import makedirs, path
from urllib.parse import urljoin, urlsplit

import scrapy
from scrapy.http import Request

from webnovel_scrapy.config.KobatoChanConfig import *
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
    file_name_list = url.split('/')
    index = -1
    while not file_name_list[index]:
        index -= 1
    return f"{file_name_list[index]}.html"


def file_exists(dir_path, url):
    name = get_novel_file_name(url)
    full_path = path.join(dir_path, name)
    return path.exists(full_path) and path.isfile(full_path)


def create_meta(full_path, novel_index):
    meta = dict()
    meta[NOVEL_LOCAL_FULL_PATH] = full_path
    meta[NOVEL_INDEX] = novel_index
    return meta


class KobatoChanSpider(scrapy.Spider):
    name = "KobatoChanSpider"

    def __init__(self, summary_url=None, **kw):
        self.summary_url = summary_url
        self.URLS = defaultdict(set)
        super(KobatoChanSpider, self).__init__(**kw)

    def start_requests(self):
        if self.summary_url:
            full_path = get_full_novel_path(self.summary_url)
            meta = create_meta(full_path, 0)
            url_request = [Request(self.summary_url, meta=meta, callback=self.parse)]
            return url_request

        print("0: Update all Novels")
        for index, novel in enumerate(NOVEL_URLS):
            print(f"{index + 1}: {novel[NOVEL_NAME]}")

        selected_index = int(input("Input= "))

        url_request = []
        if selected_index < 0 or selected_index > len(NOVEL_URLS):
            logging.warning("Wrong Index")
            return []
        elif selected_index == 0:
            for index in range(len(NOVEL_URLS)):
                summary_request = self.get_selected_novel_request(index)
                url_request.append(summary_request)
        else:
            summary_request = self.get_selected_novel_request(selected_index - 1)
            url_request.append(summary_request)
        return url_request

    def get_selected_novel_request(self, selected_index):
        selected_novel = NOVEL_URLS[selected_index]
        full_path = get_full_novel_path(selected_novel[SUMMARY_URL])
        exclude_list_set = selected_novel.get(URL_EXCLUDE_LIST, [])
        if selected_novel[CHAPTER_URL_IN_SEQUENTIAL]:
            chapter_url = selected_novel[CHAPTER_URL]
            for index in range(selected_novel[CHAPTER_START], selected_novel[CHAPTER_END] + 1):
                final_url = chapter_url.format(index)
                if final_url in exclude_list_set or file_exists(full_path, final_url):
                    continue
                self.URLS[selected_index].add(final_url)
        meta = create_meta(full_path, selected_index)
        summary_request = Request(selected_novel[SUMMARY_URL], meta=meta, callback=self.parse)
        return summary_request

    def parse(self, response):
        if response.status != 200:
            logging.warning(f"Failed to fetch URL: {response.url}")
            return

        full_path = response.meta[NOVEL_LOCAL_FULL_PATH]
        novel_index = response.meta[NOVEL_INDEX]
        meta = create_meta(full_path, novel_index)

        with open(path.join(full_path, "0_summary.html"), 'wb') as chapter_file:
            chapter_file.write(response.body)

        self.extract_urls_from_summary_page(response, full_path, novel_index)

        url_request = [Request(url, meta=meta, callback=self.parse_novel_chapter) for url in self.URLS[novel_index]]
        print(meta)
        print(self.URLS[novel_index])
        print()
        return url_request

    def extract_urls_from_summary_page(self, response, full_path, novel_index):
        parsed_content = parseHtml(response.body)
        chapter_paths_array = parsed_content.xpath(SUMMARY_PAGE_A_LINK_XPATH)
        exclude_list_set = NOVEL_URLS[novel_index].get(URL_EXCLUDE_LIST, [])
        if chapter_paths_array is None or not chapter_paths_array:
            return None
        for a_link in chapter_paths_array:
            href = a_link.get('href').strip()
            if href is None or not href:
                continue
            final_url = urljoin(response.url, href)
            if final_url in exclude_list_set or file_exists(full_path, final_url):
                continue
            self.URLS[novel_index].add(final_url)

    def parse_novel_chapter(self, response):
        if response.status != 200:
            logging.warning(f"Failed to fetch URL: {response.url}")
            return
        full_path = response.meta[NOVEL_LOCAL_FULL_PATH]
        with open(path.join(full_path, get_novel_file_name(response.url)), 'wb') as chapter_file:
            chapter_file.write(response.body)
