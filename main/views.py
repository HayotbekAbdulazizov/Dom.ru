from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from django.views.generic import TemplateView, DetailView, ListView,  View
import json







import requests
from bs4 import BeautifulSoup
import time



# list?object=flat&deal=sell&page=1&search_query=ee1b36e93e7cd7befcc1e1c318f533ac

# globalSoupStatus = requests.get("https://dom.693006.ru/list?object=flat&deal=sell&page=1")















class HomePageViews(View):
    def get(self,request):
        pageCount = 1

        for page in range(235):

            globalSoupStatus = requests.get(f"https://dom.693006.ru/list?object=flat&deal=sell&page={pageCount}")
            # time.sleep(0.3)
            globalSoup = BeautifulSoup(globalSoupStatus.text, 'html.parser')
            offerList = globalSoup.findAll("article", {"class": "list-card-desktop"})

            count = 0
            for i in offerList[0:50]:
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
                [aboutApartment, aboutHouse] = offerSectionLeft.findAll("div", {"class":"table-categoty"})
                
                offerId = int(detailSoup.find("span", {"class":"breadcrumbs-current"}).text.split()[2])
                print("ID", offerId, type(offerId))
                

            

                try:
                    Post.objects.update_or_create( offerId=offerId,
                        defaults={
                            "title":offerTitle,
                            "price":300000,
                            "priceCurrency": offerPriceCurrency,
                            "pricePerMeter": offerPricePerMeter,
                            # "city ": "Peter",
                            "address": offerAddress,
                            "description": offerDescription,
                            "body":   f"{aboutApartment}{aboutHouse}"
                    })
                    count += 1
                    print(" ---  Created Or Updated ---", count, pageCount)
                except Exception as err:
                    count += 1
                    print("---  Something went wrong --- ", count , pageCount)
                    print(err)
            pageCount += 1
        return render(request, 'index.html', {"posts":Post.objects.all()})










class HomePageView(View):
    
    def get(self,request):
        posts = Post.objects.all().order_by("-published")[:1]

        context = {
            "posts":posts
        }
        return render(request, "index.html", context)















