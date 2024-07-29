LIST_TRUE = False    # Maybe enable SAVE_HTML_WITH_DOWNLOAD  True
SKIP_NAME = False

HTML_SAVE_PATH = "/Users/gyanesh/Documents/Web Novels/websites"
HTML_FOLDER_NAME = "Lord of Mysteries 2_ Circle of Inevitability"
HTML_SAVE_ONLY_FLAG = False
SAVE_HTML_WITH_DOWNLOAD = False
USE_SELENIUM = False
SKIP_MULTI_THREADED = False

TO_BE_FORMAT_URL = None
START_PAGE = 1
END_PAGE = 320

DONT_STRIP_CHAPTER = [
]

def dont_strip(url):
    for c in DONT_STRIP_CHAPTER:
        if url.find(c) != -1:
            return True
    return False

"""
If only LIST_TRUE is true list format will be

LIST = [
    "<webnovel_url>"
]

if both LIST_TRUE and SKIP_NAME is true list format will be

LIST = [
    ["<chapter_name>", "<webnovel_url>"]
]

"""

LIST = [

]
