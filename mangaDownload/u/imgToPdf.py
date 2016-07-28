# /usr/bin
import img2pdf
import os
import re


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

root = "./pdf/"

listDir = os.listdir(root)

dirToConvert = []
for dt in listDir:
    d = root + dt
    if os.path.isdir(d) and dt != ".DS_Store":
        name = d + ".pdf"
        tempListDir = os.listdir(d)
        tempListDir.sort(key=natural_keys)
        pics = []
        for p in tempListDir:
            ppath = d + "/" + p
            if os.path.isfile(ppath) and p != ".DS_Store" and re.match(r'^.*\.(jpg|jpeg|png)$', p):
                pics.append(ppath)
        print pics
        pdf_bytes = img2pdf.convert(pics)
        file = open(name, "wb")
        file.write(pdf_bytes)