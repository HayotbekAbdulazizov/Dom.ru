import requests
from bs4 import BeautifulSoup
import time





globalSoupStatus = requests.get("https://dom.693006.ru/list?object=flat&deal=sell&page=1")
globalSoup = BeautifulSoup(globalSoupStatus.text, 'html.parser')


offerList = globalSoup.findAll("article", {"class": "list-card-desktop"})






for i in offerList[0:2]:
    title = None

    offerPrice = None
    offerPriceCurrency = None
    offerPricePerMeter = None
    offerAddress = None






    
    
    mainOfferSectionRight = None
    
    
    ahrefs = i.find("a")
    detailSoupStatus = requests.get(f"https://dom.693006.ru{ahrefs['href']}")
    detailSoup = BeautifulSoup(detailSoupStatus.text, "html.parser")
    title = detailSoup.find("h1", {"class":"offer-announce offer-announce"}).text
    
    mainOfferSectionRight = detailSoup.find("article", {"class" : "offer-main"})
    title = mainOfferSectionRight.find("h1", {"class":"offer-announce"}).text
    offerAddress = mainOfferSectionRight.find("div", {"class":"offer-address block offer-address"}).text
    offerStatus = mainOfferSectionRight.find("div", {"class":"offer-stats"})
    print(offerAddress)
    print(offerStatus)
    
    
    
    
    print()
    print()
    # print(i.find("div", {"class": "list-card-address text-darkest-grey flex y-center"}))




















# offer-main
# list-card-desktop
# content-padding
# list-card-layout
# Offer list offer-list-section-content-list w-100