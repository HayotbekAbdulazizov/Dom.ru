import requests
from bs4 import BeautifulSoup
import time





r = requests.get("https://dom.693006.ru/list?object=flat&deal=sell&page=1")
globalSoup = BeautifulSoup(r.text, 'html.parser')


offerList = globalSoup.findAll("article", {"class": "list-card-desktop"})






for i in offerList:
    i.find("a")
    print(i.find("div", {"class": "list-card-address text-darkest-grey flex y-center"}).text)







# list-card-desktop
# content-padding
# list-card-layout
# Offer list offer-list-section-content-list w-100