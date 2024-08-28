import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

url = "https://jobs.dou.ua/"


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

getMainTitles = soup.find_all("a", {"class":"cat-link"})

for cat in getMainTitles:
    print(cat.text)

val = input("Choose category")

newUrl = url + "vacancies/?category=" + val + "&exp=0-1"
print(newUrl)
page = requests.get(newUrl, headers=headers)

vacanciesSoup = BeautifulSoup(page.content, "html.parser")

getVacancies = vacanciesSoup.find_all("a", {"class":"vt"})
getLinks = ""