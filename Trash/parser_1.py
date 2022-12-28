import requests
from bs4 import BeautifulSoup
import time



# list?object=flat&deal=sell&page=1&search_query=ee1b36e93e7cd7befcc1e1c318f533ac

# globalSoupStatus = requests.get("https://dom.693006.ru/list?object=flat&deal=sell&page=1")

globalSoupStatus = requests.get("https://dom.693006.ru/list?object=flat&deal=sell&page=1&search_query=ee1b36e93e7cd7befcc1e1c318f533ac")

print(globalSoupStatus.text)
globalSoup = BeautifulSoup(globalSoupStatus.text, 'html.parser')

allPostsCountSoup = globalSoup.findAll("div", {"class":"filter-period-btn"})


allCount = allPostsCountSoup[0].text.split()[1]
allCount = allCount.replace("(", "")
allCount = allCount.replace(")", "")
# print("CCCCCCC   ", )
# print("CCCCCCC   ", allCount = )
# allCount = int(allCount)
# print(type(allCount))
# print(allCount)






offerList = globalSoup.findAll("article", {"class": "list-card-desktop"})






for i in offerList[0:2]:
    offerTitle = None
    offerPrice = None
    offerPriceCurrency = None
    offerPricePerMeter = None
    offerAddress = None
    aboutApartmentHome = None
    offerDescription = None
    offerNear = None
    videoPlayer = None
    offerMap = None
    offerId = None
    
    baseOfferSectionRight = None
    offerSectionLeft = None
    
    
    ahrefs = i.find("a")
    detailSoupStatus = requests.get(f"https://dom.693006.ru{ahrefs['href']}")
    detailSoup = BeautifulSoup(detailSoupStatus.text, "html.parser")
    offerTitle = detailSoup.find("h1", {"class":"offer-announce offer-announce"}).text
    
    offerId = detailSoup.find("span", {"class":"breadcrumbs-current"})

    baseOfferSectionRight = detailSoup.find("article", {"class" : "offer-main"})
    offerTitle = baseOfferSectionRight.find("h1", {"class":"offer-announce"}).text
    offerAddress = baseOfferSectionRight.find("div", {"class":"offer-address block offer-address"}).text
    offerStatusViews = baseOfferSectionRight.find("div", {"class":"offer-stats"}).text
    aboutApartmentHome = baseOfferSectionRight.find("div", {"class":"table"})
    offerPriceMainContainer = baseOfferSectionRight.find("div", {"class":"offer-price"})
    
    offerDescription = detailSoup.find("div", {"class":"offer-description"}).text

    offerPrice = offerPriceMainContainer.find("span", {"class":"offer-price-cost"}).text
    offerPriceCurrency = offerPriceMainContainer.find("span", {"class":"offer-price-value"}).text
    offerPricePerMeter = offerPriceMainContainer.find("span", {"class":"offer-price-period text-darkest-grey"}).text


    offerSectionLeft = detailSoup.find("section", {"class":"offer-section-left grid"})
    offerNear = offerSectionLeft.find("article", {"class":"offer-near"})
    # tableCategoriesApartmentHome = offerSectionLeft.findAll("div", {"class":"table-categoty"})
    videoPlayer = offerSectionLeft.find("section", {"class":"offer-info-videoplayer"})
    offerMap = offerSectionLeft.find("article", {"class":"offer-map"})
    # print(offerMap)
    [aboutApartment, aboutHouse] = offerSectionLeft.findAll("div", {"class":"table-categoty"})
    
    
    
    # print("title -",offerTitle)
    # print("price - ", offerPrice)
    # print("price cur - " , offerPriceCurrency)
    # print("price pm - ", offerPricePerMeter)
    # print("Address - ", offerAddress)
    # print("About apartment   ",aboutApartment.text)
    # print("About Home  - ", aboutHouse.text)
    # print("Description - ", offerDescription)
    # print("Near : ", offerNear)
    # inttt = int(offerId.text.split()[2])
    # print(inttt)
    # print(type(inttt))
    print()
    print()

    # print(i.find("div", {"class": "list-card-address text-darkest-grey flex y-center"}))




















# offer-main
# list-card-desktop
# content-padding
# list-card-layout
# Offer list offer-list-section-content-list w-100