## Download Chapters from WuxiaWorld

#### Directly using summary page url

```bash
$ scrapy crawl WuxiaWorldDownloadSpider -a summary_url=<wuxia_worl_summary_page_url>
```

------

#### Creating a Novel entry in the Config

At the end [WuxiaWorldDownloadConfig.py](./webnovel_scrapy/config/WuxiaWorldDownloadConfig.py) add the following entry:

```python
NOVEL_URLS.append({
    NOVEL_NAME: "Renegade Immortal",
    SUMMARY_URL: "https://www.wuxiaworld.com/novel/renegade-immortal",
    CHAPTER_URL_IN_SEQUENTIAL: True			# If this is True then only following are useful
    CHAPTER_URL: "https://www.wuxiaworld.com/novel/renegade-immortal/rge-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 2089,
})
```

Then run

```bash
$ scrapy crawl WuxiaWorldDownloadSpider
```

------

## Recreating Conda Environment

```bash
$ conda env create -f environment.yml
```

