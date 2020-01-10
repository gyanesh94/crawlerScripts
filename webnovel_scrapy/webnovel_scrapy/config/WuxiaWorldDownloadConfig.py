# Basic File Location Constants
BASE_PATH = "/Users/gyanesh/Documents/Web Novels/websites"

# Constants
NOVEL_NAME = "name"
SUMMARY_URL = "summary_url"
CHAPTER_URL = "chapter_url"
CHAPTER_START = "chapter_start"
CHAPTER_END = "chapter_end"
CHAPTER_URL_IN_SEQUENTIAL = "sequential"
URL_EXCLUDE_LIST = "exclude_list"
NOVEL_INDEX = "novel_index"

NOVEL_LOCAL_FULL_PATH = "full_path"

# XPath Constants
SUMMARY_PAGE_A_LINK_XPATH = "//div[@class='panel-group']//div[@class='panel-body']//a"

# Novels Data
NOVEL_URLS = []

NOVEL_URLS.append({
    NOVEL_NAME: "Renegade Immortal",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/renegade-immortal",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 2089,
    URL_EXCLUDE_LIST: (
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-0',
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-1455',
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-17405',
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-717',
        'https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-1740',
    )
})

NOVEL_URLS.append({
    NOVEL_NAME: "Desolate Era",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/desolate-era",
    CHAPTER_URL_IN_SEQUENTIAL: False
})

NOVEL_URLS.append({
    NOVEL_NAME: "Trash of the Count's Family",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/trash-of-the-counts-family",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/trash-of-the-counts-family/tcf-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 444
})

NOVEL_URLS.append({
    NOVEL_NAME: "Rebirth of the Thief Who Roamed the World",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/rebirth-of-the-thief-who-roamed-the-world",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/rebirth-of-the-thief-who-roamed-the-world/rotwrtw-chapter-{}",
    CHAPTER_START: 1,
    CHAPTER_END: 959
})
