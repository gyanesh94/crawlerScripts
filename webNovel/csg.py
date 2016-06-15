#!/usr/bin/python

"""
1. Against The God
2. Skyfire Avenue
3. Martial God Asura
4. The Great Ruler
5. Tales Od Demons And Gods
6. Coiling Dragon
7. I Shall Seal the Heavens
8. Chaotic God Sword (Beware Of Comments)
8. Desolate Era
9. Stellar Transformations
"""

from bs4 import BeautifulSoup
import urllib2
import urllib
import os
import sys, getopt
import re


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

def str_encode(name):
	name = name.strip()
	name = name.replace(':','-')
	name = name.encode(encoding='unicode_escape')
	name = name.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", '--')
	return name


def url_encode(url):
	url = url.strip()
	url = url.encode(encoding='unicode_escape')
	url = url.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
	return url


def get_chapters(chapters):
	links = []
	for chapter in chapters:
		href = chapter['href']
		href = url_encode(href)
		name = chapter.string
		name = str_encode(name)
		links.append([href,name])
	return links


def save_chapter(name, content):
	# name= "/Users/gyanesh/Documents/.a/Web Novel alias/csg/" + name
	name = "untitled folder/" + name
	text = open(name+".txt", "w")
	text.write(content)
	text.close()

def get_content(url):
	src = get_src(url)
	soup = BeautifulSoup(src, 'html.parser')
	div = soup.find("div", {"class": "entry-content"})
	p = div.find_all("p")
	p = p[1:]
	# Name Extraction
	name = p[0]
	name = name.get_text()
	name = re.sub(r'^.*Chapter ', '', name)
	name = re.sub(r':', '-', name)

	# Body Extraction
	p = p[1:]
	content = ""
	for i in p:
		if i.sup:
			if i.sup.a:
				i.sup.a.unwrap()
			i.sup.unwrap()
		if i.strong:
			i.strong.unwrap()
		if i.em:
			i.em.unwrap()
		t = i.get_text()
		content += t + "\n\n"
	content = re.sub(r'(.*)Previous (Chapter)?\s*Next Chapter(.*)', r'\1\n\3', content)
	content = content.strip()

	# Foot note Extraction
	foot = div.find("div", {"class": "footnotes"})
	if foot:
		content += "\n\n" + "-----------" + "\n"
		lis = foot.find_all("li")
		i = 1
		for li in lis:
			if li.span:
				li.span.decompose()
			content += str(i) + "." + li.get_text() + "\n"
			i += 1
		content = content.strip()
	return name, content.encode("utf-8")

def get_urls():
	url = "http://gravitytales.com/chaotic-sword-god/csg-chapter-{}/"
	start = input("Start= ")
	end = input("End= ")
	l = []
	for i in range(start, end + 1):
		l += [url.format(i)]
	return l

urls = get_urls()

# urls = [get_url()]

for url in urls:
	name, content = get_content(url)
	save_chapter(name, content)

# src = get_src(url)
# soup = BeautifulSoup(src, 'html.parser')
# div = soup.find("div", {"class": "entry-content"})
# chapters = get_chapters(div.find_all("a"))