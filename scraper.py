import time
import re
import csv
import os
from videogame import VideoGame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime

# TODO better error handling, multithreading

def pullVals(console):
    try:
        SCROLL_PAUSE_TIME = 1

        # Scrolls to bottom of website to load all values for console
        browser = webdriver.Firefox() #TODO add support for multiple browsers
        browser.get('https://www.pricecharting.com/console/' + console)
        prevHeight = browser.execute_script("return document.body.scrollHeight")
        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            currHeight = browser.execute_script("return document.body.scrollHeight")
            if prevHeight == currHeight:
                break
            prevHeight = currHeight

        # Parses video game information
        games = []
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for EachPart in soup.select('tr[id*="product-"]'):
            title = re.search(r'>(.*?)</a>', str(EachPart.select('td[class="title"]'))).group(1)
            loosePrice = re.findall("\d+\.\d+", str(EachPart.select('td[class="price numeric used_price"]')))
            loosePrice = loosePrice[0] if len(loosePrice) > 0 else "N/A"
            completePrice = re.findall("\d+\.\d+", str(EachPart.select('td[class="price numeric cib_price"]')))
            completePrice = completePrice[0] if len(completePrice) > 0 else "N/A"
            newPrice = re.findall("\d+\.\d+", str(EachPart.select('td[class="price numeric new_price"]')))
            newPrice = newPrice[0] if len(newPrice) > 0 else "N/A"
            newGame = VideoGame(title, console, loosePrice, completePrice, newPrice)
            games.append(newGame)
        return games
    except:
        return []

def gameCsv(games):
    dt = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
    fn = "game_prices.csv"
    if not os.path.exists(dt):
        os.mkdir(dt)
    with open(os.path.join(dt, fn), 'w') as csv_file:
        fieldnames = ['game', 'console', 'loose_val', 'complete_val', 'new_val', 'date(D/M/Y)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for g in games:
            writer.writerow({'game': g.getTitle(), 'console': g.getConsole(), 'loose_val': g.getLoosePrice(), 'complete_val': g.getCompletePrice(),
            'new_val': g.getNewPrice(), 'date(D/M/Y)': dt.split('_')[0].replace('.', '/')})

def main():
    """Sets directory name to current data and time, filename to "game_prices.csv" and orders execution of our program
    """
    consoles = ["super-nintendo", "nes", "nintendo-64", "gamecube", "wii", "wii-u", "nintendo-switch", "gameboy", "gameboy-color",
        "gameboy-advance", "nintendo-ds", "nintendo-3ds", "virtual-boy", "game-&-watch", "playstation", "playstation-2", "playstation-3",
        "playstation-4", "psp", "playstation-vita", "sega-master-system", "sega-genesis", "sega-cd", "sega-32x", "sega-saturn",
        "sega-dreamcast", "sega-game-gear", "xbox", "xbox-360", "xbox-one", "atari-2600", "atari-5200", "atari-7800", "atari-lynx", "jaguar"]
    allGames = []
    for console in consoles:
        consoleGames = pullVals(console)
        for game in consoleGames:
            allGames.append(game)
    gameCsv(allGames)

if __name__== "__main__":
    """Entry point for our program
    """
    main()