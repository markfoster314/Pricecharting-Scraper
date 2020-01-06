import requests
import re
from bs4 import BeautifulSoup


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

def main():
    consoles = ["nes", "super-nintendo", "nintendo-64", "gamecube", "wii", "wii-u", "nintendo-switch", "gameboy", 
      "gameboy-color", "gameboy-advance", "nintendo-ds", "nintendo-3ds", "virtual-boy", "game-&-watch"]
    priceArr = scrape_pricecharting(consoles[0], "super-mario-bros-3")

if __name__== "__main__":
    main()