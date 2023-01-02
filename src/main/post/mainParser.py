from countTest import countsDetector
import json
import requests
from bs4 import BeautifulSoup
import time





linksAll = {
    "https://domik65.ru/list?object=flat&deal=sell&page=1",
    "https://domik65.ru/list?object=flat&deal=lease&s%5Bperiod%5D=%D0%BF%D0%BE%D1%81%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%BE&page=1",
    "https://domik65.ru/list?object=flat&deal=sell&s%5Brecom_filter%5D%5B0%5D=1&page=1",
    "https://domik65.ru/list?object=flat&deal=lease&s%5Bperiod%5D=%D0%B5%D0%B6%D0%B5%D0%BC%D0%B5%D1%81%D1%8F%D1%87%D0%BD%D0%BE&s%5Brecom_filter%5D%5B0%5D=1&page=1",
    "https://domik65.ru/list?object=house&deal=sell&page=1",
    "https://domik65.ru/list?object=business&deal=sell&page=1"
}


linksDaily = [
    "https://domik65.ru/list?object=flat&deal=sell&page=1&search_query=ee1b36e93e7cd7befcc1e1c318f533ac",
    "https://domik65.ru/list?object=flat&deal=lease&s%5Bperiod%5D=%D0%BF%D0%BE%D1%81%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%BE&page=1&search_query=528984f74264b1bb7c144b98c1a1671d",
    "https://domik65.ru/list?object=flat&deal=sell&s%5Brecom_filter%5D%5B0%5D=1&page=1&search_query=ec85391999e793342c9fb78e9731de52",
    "https://domik65.ru/list?object=flat&deal=lease&s%5Bperiod%5D=%D0%B5%D0%B6%D0%B5%D0%BC%D0%B5%D1%81%D1%8F%D1%87%D0%BD%D0%BE&s%5Brecom_filter%5D%5B0%5D=1&page=1&search_query=73998f8caf727ab2e231baef316d5ab2",
    "https://domik65.ru/list?object=house&deal=sell&page=1&search_query=06c025c0cb9efc0285347359d30b4d7e",
    "https://domik65.ru/list?object=business&deal=sell&page=1&search_query=a8fca08f4862252563499075b35225dd"
]








def parse():
    
    for linkDaily in linksDaily:
        print()
        print(" =========  ", linkDaily)
        numberOfPagesInLink = countsDetector(linkDaily)
        print(numberOfPagesInLink)

        print("Number of pages  == ", numberOfPagesInLink)
        # for pageCount in range(0, numberOfPagesInLink + 1):
        for pageCount in range(1, numberOfPagesInLink + 1):

            globalSoupStatus = requests.get(linkDaily.replace("page=1", f"page={pageCount}"))
            time.sleep(0.3)
            globalSoup = BeautifulSoup(globalSoupStatus.text, 'html.parser')
            offerList = globalSoup.findAll("article", {"class": "list-card-desktop"})

            count = 0
            for i in offerList[0:50]:
                offerTitle = None
                offerPrice = None
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
                detailSoupStatus = requests.get(f"https://domik65.ru{ahrefs['href']}")
                # time.sleep(0.3)
                detailSoup = BeautifulSoup(detailSoupStatus.text, "html.parser")
                offerTitle = detailSoup.find("h1", {"class":"offer-announce offer-announce"}).text

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
                
                [aboutApartment, aboutHouse] = offerSectionLeft.findAll("div", {"class":"table-category"})

                offerId = int(detailSoup.find("span", {"class":"breadcrumbs-current"}).text.split()[2])
                print("ID", offerId, type(offerId))




                try:
                    print("title - ", offerTitle)
                    print("Id - ", offerId)
                    count += 1
                    print(" ---  Created Or Updated ---", count, pageCount)
                except Exception as err:
                    count += 1
                    print("---  Something went wrong --- ", count , pageCount)
                    print(err)
            pageCount += 1






















parse()