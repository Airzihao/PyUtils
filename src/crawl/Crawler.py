from bs4 import BeautifulSoup
import urllib
import os
import time
import random

urlDict = {"pvldb12" : "https://dblp.uni-trier.de/db/journals/pvldb/pvldb12.html",
       "pvldb11" : "https://dblp.uni-trier.de/db/journals/pvldb/pvldb11.html",
       "pvldb10" : "https://dblp.uni-trier.de/db/journals/pvldb/pvldb10.html",
       "pvldb9" : "https://dblp.uni-trier.de/db/journals/pvldb/pvldb9.html",
       "pvldb8" : "https://dblp.uni-trier.de/db/journals/pvldb/pvldb8.html",
       "pvldb7" : "https://dblp.uni-trier.de/db/journals/pvldb/pvldb7.html"}

count = 0

def getHtmlText(url):
    text = urllib.request.urlopen(url).read()
    return text

def collectLink(url, fileName):
    pdfLinkSet = set()
    text = getHtmlText(url)
    soup = BeautifulSoup(text, 'html.parser')
    for tag in soup("a"):
        link = tag.get("href")
        linkStr = str(link)
        if (linkStr.startswith("http://www.vldb") and linkStr.endswith(".pdf")):
            pdfLinkSet.add(linkStr)

    if(os.path.exists("./vldb/" + fileName) == False):
        os.makedirs("./vldb/" + fileName)
    with open("./vldb/" + fileName +"/" + fileName +".txt", "w+") as linkFile:
        print(len(pdfLinkSet))
        for item in pdfLinkSet:
            time.sleep(random.randint(5,10))
            global count
            count = count+1
            print("Downloading "+str(count)+"th of 1314 files...")
            download("./"+fileName, item)
            linkFile.write(item + "\n")

def getAllPdfFiles(urlDict: dict):
    for key, value in urlDict.items():
        volName = key
        url = value
        collectLink(url, volName)

def download(targetDir, url):
    filePath = targetDir+ "/" + os.path.basename(url)
    if(os.path.exists(targetDir) == False):
        os.makedirs(targetDir)
    try:
        pdf = urllib.request.urlopen(url, timeout=60).read()
        with open(filePath, "wb+") as file:
            file.write(pdf)
    except Exception as e:
        with open("./failedRecord.txt", "w+") as failRecord:
            failRecord.write(url)

if __name__ == '__main__':
    getAllPdfFiles(urlDict)