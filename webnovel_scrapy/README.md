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


## Download Chapters from [kobatochan](https://kobatochan.com/)

#### Directly using summary page url

```bash
$ scrapy crawl KobatoChanSpider -a summary_url=<kobato_chan_summary_page_url>
```

------

#### Creating a Novel entry in the Config

At the end [KobatoChanConfig.py](./webnovel_scrapy/config/KobatoChanConfig.py) add the following entry:

```python
NOVEL_URLS.append({
    NOVEL_NAME: "Everyone Else is a Returnee",
    SUMMARY_URL: "https://kobatochan.com/korean-novels/everyone-else-is-a-returnee/",
    CHAPTER_URL_IN_SEQUENTIAL: True,
    CHAPTER_URL: "https://kobatochan.com/everyone-else-is-a-returnee-chapter-{}",
    CHAPTER_START: 0,
    CHAPTER_END: 352
})
```

Then run

```bash
$ scrapy crawl KobatoChanSpider
```

------

## Recreating Conda Environment

```bash
$ conda env create -f environment.yml
```

