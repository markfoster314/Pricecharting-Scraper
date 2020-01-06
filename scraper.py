import requests
import re
from bs4 import BeautifulSoup


def scrape_pricecharting(console, game):
    """Scrapes game market value from pricecharting.com

    Args:
      console: game system name
      game:    title of video game

    Returns:
      list of the cartridges values
    """
    page = requests.get("https://www.pricecharting.com/game/" + console + "/" + game)
    soup = BeautifulSoup(page.content, 'html.parser')

    allPrices = list(list(list(soup.children)[15])[1])
    cartPrice = float(re.findall("\d+\.\d+", str(list(list(allPrices[1])[1])[0].encode('utf-8')))[0])
    completePrice = float(re.findall("\d+\.\d+", str(list(list(allPrices[3])[1])[0].encode('utf-8')))[0])
    sealedPrice = float(re.findall("\d+\.\d+", str(list(list(allPrices[5])[1])[0].encode('utf-8')))[0])
    gradedPrice = float(re.findall("\d+\.\d+", str(list(list(allPrices[7])[1])[0].encode('utf-8')))[0])
    boxPrice = float(re.findall("\d+\.\d+", str(list(list(allPrices[9])[1])[0].encode('utf-8')))[0])
    manualPrice = float(re.findall("\d+\.\d+", str(list(list(allPrices[11])[1])[0].encode('utf-8')))[0])

def main():
    scrape_pricecharting("nes", "super-mario-bros-3")

if __name__== "__main__":
    main()