from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

URL="https://store.steampowered.com/app/2778580/ELDEN_RING_Shadow_of_the_Erdtree/"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    }
class SoupManager:
    def __init__(self):
       # self.response = requests.get(url=URL,headers=header)
       driver = webdriver.Chrome()
       url = "https://store.steampowered.com/app/2778580/ELDEN_RING_Shadow_of_the_Erdtree/"
       driver.maximize_window()
       driver.get(url)

       time.sleep(5)
       content = driver.page_source.encode('utf-8').strip()
       self.soup = BeautifulSoup(content, "html.parser")



    def get_price(self):
        price = self.soup.find(name="div", class_="game_purchase_price price").getText()
        new_price = price.replace("$", "").replace(" USD", "").strip()

        print(new_price)
        return float(new_price)


    def check_price(self):
        if self.get_price() < 26:
            return True
        else:
            return False

