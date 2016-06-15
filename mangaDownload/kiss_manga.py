#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2
import urllib
import os
import sys, getopt


def get_url():
	url = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"u:")
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
	name = name.replace(':','-')
	name = name.encode(encoding='unicode_escape')
	name = name.replace("\u2018", "'").replace("\u2019", "'")
	return name


def get_chapters(chapters, url):
	links = []
	for chapter in chapters:
		href = chapter['href']
		index = href.rindex('/')
		href = url + href[index:]
		href = url_encode(href)
		name = chapter.string
		name = str_encode(name)
		links.append([href,name])
	return links


def get_image_links(url):
	src = get_src(url)
	soup = BeautifulSoup(src, 'html.parser')
	script = soup.find_all('script')
	script = script[7].string
	temp = script.find("lstImagesLoaded")
	script = script[:temp]
	start = script.find('http:')
	pages = []
	while start <> -1:
		end = script.find('")', start)
		link = script[start:end]
		start = script.find('http:',end)
		name = link.split("/")[-1]
		pages.append([link, name])
	return pages


def get_images(href,name):
	pages = get_image_links(href)
	os.mkdir(name)
	os.chdir(name)
	for page in pages:
		urllib.urlretrieve(page[0],page[1])
	os.chdir("..")


url = get_url()

if url:
	src = get_src(url)
	soup = BeautifulSoup(src, 'html.parser')
	chapters = get_chapters(soup.table.find_all('a'), url)
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
					get_images(chapter[0],chapter[1])
			elif ch == "r" or ch == "R":
				for i in range(int(choices[1]), int(choices[2]) + 1):
					chapter = chapters[i]
					get_images(chapter[0],chapter[1])
			else:
				choices = filter(lambda x: x.isdigit() , choices)
				if choices:
					choices = map(lambda x: int(x), choices)
					for choice in choices:
						chapter = chapters[choice]
						get_images(chapter[0],chapter[1])