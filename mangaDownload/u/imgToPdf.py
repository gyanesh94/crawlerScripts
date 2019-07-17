import img2pdf
import os
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


root = "/Users/gyanesh/Documents/Anime Manga/Unread/"


def convertToPdf(d):
    name = d + ".pdf"
    tempListDir = os.listdir(d)
    tempListDir.sort(key=natural_keys)
    pics = []
    for p in tempListDir:
        ppath = os.path.join(d, p)
        if os.path.isfile(ppath) and p != ".DS_Store" and re.match(r'^.*\.(jpg|jpeg|png)$', p):
            pics.append(ppath)
    print pics
    if not pics:
        return
    pdf_bytes = img2pdf.convert(pics)
    file = open(name, "wb")
    file.write(pdf_bytes)


def checkFolderToConvert(root):
    listDir = os.listdir(root)
    for dt in listDir:
        d = os.path.join(root, dt)
        if os.path.isdir(d) and dt != ".DS_Store":
            convertToPdf(d)

if __name__ == '__main__':
    checkFolderToConvert(root)
