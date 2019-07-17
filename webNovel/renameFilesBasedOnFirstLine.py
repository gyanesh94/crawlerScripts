# -*- coding: utf-8 -*-
# Renaming the files from all directories in the given folder

import os
import re

BASE_DIR = "/Users/gyanesh/Documents/Web Novels/Web Novel alias/rename"

RENAME_FILE = False

ignored = {".DS_Store"}
# folders = [x for x in os.listdir(path) if x not in ignored]

def renameFiles():
    filesList = [x for x in os.listdir(BASE_DIR) if x not in ignored]
    for fileName in filesList:
        fileNamePath = os.path.join(BASE_DIR, fileName)
        if os.path.exists(fileNamePath) and os.path.isfile(fileNamePath) and fileName != "" and fileName.find('txt') != -1:
            newName = ""
            with open(fileNamePath, 'r') as f:
                newName = f.readlines()[0]
            
            newName = newName.decode('utf-8')
            newName = newName.replace(u"\xa0", u" ").replace(u"\u3000", u" ").replace(u"\u2013", u"-").replace(u"/", u"-").replace(u"\\", u" -").replace(u'\u2019', "'").replace(u'\u2018', "'").replace(u'\u201D', '"').replace(u'\u201C', '"')
            newName = newName.encode('utf-8')

            if re.findall('(?:\s|-|^)[0-9]{1,5}(?:\s|-)', newName) != []:
                newName = re.sub(r' [ ]+', r' ', newName)
                newName = re.sub(r':', '-', newName)
                newName = newName.split("Chapter")
                if len(newName) > 1:
                    del newName[0]
                newName = "Chapter".join(newName)
                # name = re.sub(r'^[\w\s\S\W]*Chapter\s', '', name, 1)
                newName = re.sub(r'^AST ([0-9]{1,5})', r'\1', newName)
                newName = re.sub(r'^0+', '', newName)
                newName = newName.strip()
            
                print("oldName: {}\t newName: {}".format(fileName, newName))
                newFilePath = os.path.join(BASE_DIR, newName + ".txt")
                if RENAME_FILE:
                    os.rename(fileNamePath, newFilePath)


if __name__ == '__main__':
    renameFiles()
