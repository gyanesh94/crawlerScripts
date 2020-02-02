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
# Absolute
# SUMMARY_PAGE_A_LINK_XPATH = "/html/body/div[1]/div[3]/div/div/div[1]/div[1]/div/article/div/p/a"

# Relative
SUMMARY_PAGE_A_LINK_XPATH = "//div[@id='content']//div[@class='entry-content']//a"

# Novels Data
NOVEL_URLS = []
COMPLETED_NOVEL_URLS = []
PREVIEW_NOVEL_URLS = []

NOVEL_URLS.append({
    NOVEL_NAME: "Everyone Else is a Returnee",
    SUMMARY_URL: "https://kobatochan.com/korean-novels/everyone-else-is-a-returnee/",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://kobatochan.com/everyone-else-is-a-returnee-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 352
})
