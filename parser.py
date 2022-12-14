import requests
from bs4 import BeautifulSoup
import time





globalSoupStatus = requests.get("https://dom.693006.ru/list?object=flat&deal=sell&page=1")
globalSoup = BeautifulSoup(globalSoupStatus.text, 'html.parser')


offerList = globalSoup.findAll("article", {"class": "list-card-desktop"})






for i in offerList[0:2]:
    offerTitle = None
    offerPrice = None
    offerPriceCurrency = None
    offerPricePerMeter = None
    offerAddress = None
    aboutApartmentHome = None



    
    baseOfferSectionRight = None
    offerSectionLeft = None
    
    
    ahrefs = i.find("a")
    detailSoupStatus = requests.get(f"https://dom.693006.ru{ahrefs['href']}")
    detailSoup = BeautifulSoup(detailSoupStatus.text, "html.parser")
    offerTitle = detailSoup.find("h1", {"class":"offer-announce offer-announce"}).text
    
    baseOfferSectionRight = detailSoup.find("article", {"class" : "offer-main"})
    offerTitle = baseOfferSectionRight.find("h1", {"class":"offer-announce"}).text
    offerAddress = baseOfferSectionRight.find("div", {"class":"offer-address block offer-address"}).text
    offerStatus = baseOfferSectionRight.find("div", {"class":"offer-stats"}).text
    aboutApartmentHome = baseOfferSectionRight.find("div", {"class":"table"})

    offerSectionLeft = detailSoup.find("section", {"class":"offer-section-left grid"})
    tableCategoriesApartmentHome = offerSectionLeft.find("div", {"class":"table-categoty"}).text
    print("OOO   ",tableCategoriesApartmentHome)

    print(offerAddress)
    # print(offerStatus)
    print(aboutApartmentHome)    
    
    
    
    print()
    print()
    # print(i.find("div", {"class": "list-card-address text-darkest-grey flex y-center"}))




















# offer-main
# list-card-desktop
# content-padding
# list-card-layout
# Offer list offer-list-section-content-list w-100