import math
import re
import requests
from bs4 import BeautifulSoup



# //*[@id="root"]/main/section/div[1]/div[1]/div/div[2]
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


countsDetector("https://domik65.ru/list?object=flat&deal=sell&page=1&search_query=ee1b36e93e7cd7befcc1e1c318f533ac")
countsDetector("https://domik65.ru/list?object=flat&deal=sell&page=1")


  