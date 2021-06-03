import requests
import sys
from bs4 import BeautifulSoup
import pandas as pd
from bs4 import BeautifulSoup
from pykakasi import kakasi
import re

#webページを取得して解析する(企業情報)
load_url = input()
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
souptexts = soup.text

#メール
chap04 = None
for mailtext in souptexts.split("\n"):
    if re.search(r'[\w\.-]+@[\w\.-]+', mailtext):
        chap04 = re.search(r'[\w\.-]+@[\w\.-]+', mailtext)
        chap04 = chap04.group(0)
        print(chap04)
        sys.exit()
    else:
        chap04 = None

chap05 = None
for mailahref in soup.find_all("a"):
    mailahref = mailahref.get("href")
    if re.search(r'[\w\.-]+@[\w\.-]+', mailahref):
        chap05 = re.search(r'[\w\.-]+@[\w\.-]+', mailahref)
        chap05 = chap05.group(0)
        print(chap05)
        sys.exit()
    else:
        chap05 = None

if chap04 == None and chap05 == None:
    print("なし")


    print(chap05)
