import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

SCROLL_PAUSE_TIME = 2

if __name__ == "__main__":
    browser = webdriver.Firefox()

    browser.get('https://www.pricecharting.com/console/super-nintendo')
    assert 'NES' in browser.title

    prevHeight = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        currHeight = browser.execute_script("return document.body.scrollHeight")
        if prevHeight == currHeight:
            break
        prevHeight = currHeight

    soup = BeautifulSoup(browser.page_source, 'html.parser')


    for EachPart in soup.select('tr[id*="product-"]'):
        # print (EachPart.get_text())
        for used in EachPart.select('td[class="price numeric used_price"]'):
            print (used.get_text)
        # print (EachPart.select('td[class="price numeric used_price"]').get_text)

    # used = soup.find_all('tr', attrs={'id': 'price numeric used_price'})
    # print (len(used))