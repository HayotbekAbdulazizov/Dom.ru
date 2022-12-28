from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests



# Firefox
# from selenium.webdriver.firefox.options import Options


# CHrome
from selenium.webdriver.chrome.options import Options as Coptions
import chromedriver_autoinstaller





def telegram_bot_sendtext(bot_message):
    bot_token = '5952176845:AAGND8I3Vnf4FX80yZGUtd_9Ea1-9oL-77s'
    bot_chatID = '-1001566648408'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)








# Chrome
choptions = Coptions()
choptions.headless = True
driver = webdriver.Chrome(options=choptions)


# Firefox
# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)










lst = [
    "https://dom.693006.ru/flat/sell/708917",
    "https://dom.693006.ru/flat/sell/706190",
    "https://dom.693006.ru/flat/sell/708917",
    "https://dom.693006.ru/flat/sell/708121",
]



for xuy in lst:

    time.sleep(0.5)
    status = driver.get(xuy)
    # print(status)
    time.sleep(1.5)
    plt = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/section[2]/section[3]/article/article/div[4]/a').click()
    time.sleep(1.5)
    contactContainer = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/section[2]/section[3]/article/article/div[4]')
    time.sleep(1.5)


    contactContainerHtml = contactContainer.get_attribute("innerHTML")
    contactSoup = BeautifulSoup(contactContainerHtml, 'html.parser')

    numberList = contactSoup.findAll("div", {"class":"flex flex-wrap contacts-pb"})
    # print(numberList[0].text)

    phones = ''

    for ph in numberList:
        numlist1 = ph.find("a", {"class":"contacts-data"})
        phones += f"\n {numlist1['href']}"

    print(phones)
    time.sleep(0.2)
    telegram_bot_sendtext(phones)
    time.sleep(0.5)









# ip: 194.233.160.68
# password: mashxurbek

# wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodri
# wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz