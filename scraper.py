import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import os


def scrape_pricecharting(console, game):
    """Scrapes game market values from pricecharting.com

    Args:
      console: game system name
      game:    title of video game

    Returns:
      list of floats representing game prices [cartridge, CIB, sealed, graded, box, manual]
    """

    page = requests.get("https://www.pricecharting.com/game/" + console + "/" + game)
    soup = BeautifulSoup(page.content, 'html.parser')
    allPrices = list(list(list(soup.children)[15])[1])
    return [float(re.findall("\d+\.\d+", str(list(list(allPrices[2 * i + 1])[1])[0].encode('utf-8')))[0]) for i in range(6)]

# game,date,loose_value,complete_value,new_value,graded_value,box_value,manual_value

def main():
    # consoles = os.listdir('Games/')
    consoles = [console[:len(console) - 4] for console in os.listdir('Games/')]
    for x in consoles:
      print (x)

if __name__== "__main__":
    main()