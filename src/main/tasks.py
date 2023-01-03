from selenium import webdriver
import time


from selenium.webdriver.common.by import By



from domru.celery import app
from .models import Post, Contact
from datetime import datetime

import json
import requests
from bs4 import BeautifulSoup
import time

import math
import re



from celery import shared_task






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






def countsDetector(link):
    countStatus = requests.get(link)
    countSoup = BeautifulSoup(countStatus.text, "html.parser")
    count = countSoup.findAll("div", {"class": "filter-period-btn text-light-blue border-radius text-align-center bg-blue-grey"})
    if(len(count)):
        cn = re.findall(r'\d+', count[0].text)
        num = list(map(int, cn))
        result = math.ceil(num[0] / 20)
        return int(result)
    else:
        return 0












@shared_task(name="testprint")
def testprint():
    print("===== TEST print ====")
    return True


@shared_task(name="testprint2")
def testprint2():
    print("===== LALALALAAL ====")
    return True











# @app.task #регистриуем таску
@shared_task(name="parse_posts")
def parse_posts():

    for linkDaily in linksAll:
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

                offerSource = None

                baseOfferSectionRight = None
                offerSectionLeft = None


                ahrefs = i.find("a")
                offerSource = f"https://domik65.ru{ahrefs['href']}"
                detailSoupStatus = requests.get(offerSource)
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
                    post = Post.objects.update_or_create( offerId=offerId,
                    defaults={
                    "title":offerTitle,
                    # "price":offerPrice,
                    "price":100000,
                    "slug":offerId,
                    "priceCurrency": offerPriceCurrency,
                    "pricePerMeter": offerPricePerMeter,
                    # "city ": "Peter",
                    "address": offerAddress,
                    "description": offerDescription,
                    "source":offerSource,
                    "body":   f"{aboutApartment}{aboutHouse} <br> {offerNear} <br> {offerStatusViews}"
                    })

                    # Contact.objects.create(post_id=post)

                    print("title - ", offerTitle)
                    print("Id - ", offerId)
                    count += 1
                    print(" ---  Created Or Updated ---", count, pageCount)
                except Exception as err:
                    count += 1
                    # print("---  Something went wrong --- ", count , pageCount)
                    print(err)
            pageCount += 1


    return "необязательная заглушка"
























from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@shared_task(name="save_contacts")
def save_contacts():

    chrome_optio = webdriver.ChromeOptions()
    chrome_optio.add_argument("--headless")
    chrome_optio.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_optio)
    # driver = webdriver.Chrome(options=chrome_optio)



    # Authorization
    driver.get("https://domik65.ru/")    
    print(driver.title)

    btns = driver.find_elements(By.XPATH, '//*[@id="root"]/header[1]/div[1]/div/a')
    btns[0].click()
    time.sleep(3) #Error

    name_input = driver.find_element(By.XPATH, '//*[@id="login-form"]/input[3]')
    password = driver.find_element(By.XPATH, '//*[@id="login-form"]/input[4]')
    name_input.send_keys("9168157216")
    password.send_keys("qwerty12345")

    submit = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')
    submit.submit()
    time.sleep(1)



## Home page
    for i in Post.objects.filter(contacts=False):
        
        ## request to detali page 
        driver.get(i.source)
        time.sleep(1)
        # showContactButton = driver.find_element(By.CSS_SELECTOR, '#root > main > section.offer-section.grid > section.offer-side.offer-section-right.no-print > article > article > div.contacts-layout.offer-contacts > a')
        print(driver.current_url, "     =====")
        showContactButton = None
        try:
            showContactButton = driver.find_element(By.XPATH, '//*[@id="root"]/main/section[2]/section[3]/article/article/div[4]/a')
        except Exception:
            showContactButton = driver.find_element(By.CSS_SELECTOR, '#root > main > section.offer-section.grid > section.offer-side.offer-section-right.no-print > article > article > div.contacts-layout.offer-contacts > a')
        except:
            showContactButton = driver.find_element(By.XPATH, '//*[@id="root"]/main/section[2]/section[3]/article/article/div[3]/a')


        showContactButton.click()

        time.sleep(1)
        globalSoup = BeautifulSoup(driver.page_source, 'html.parser')
        time.sleep(0.5)
        contactss = globalSoup.find("div", {"class":"contacts"})
        # print(contactss)
        # print("== Type ", type(contactss))
        # print(contactss.get_attribute_list("innerHTML"), "eeee")
        innerhtml = "".join([str(x) for x in contactss.contents]) 
        print(innerhtml)
        overallBody = i.body + f"c - {innerhtml}"
        i.body = overallBody    
        i.contacts = True
        i.save()
        # time.sleep(1)
        print("------------", i.contacts)

    context = {
        "posts":Post.objects.all(),
    }
    print(" --- some")