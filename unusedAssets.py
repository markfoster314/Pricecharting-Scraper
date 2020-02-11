#todo use webscraping to pull all the links from pricecharting.com so I don't have to put them in manually

import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import os
import random
import time
from datetime import datetime
import csv
import urllib


def scrape_pricecharting(console, game):
  """Scrapes game market values from pricecharting.com

  Args:
    console: (string) game system name as it appears in the pricecharting URL
    game: (string) title of video game as it appears in the pricecharting URL

  Returns:
    (list) game prices [cartridge, CIB, sealed, graded, box, manual]
  """
  page = requests.get("https://www.pricecharting.com/game/" + console + "/" + game)
  soup = BeautifulSoup(page.content, 'html.parser')
  allPrices = list(list(list(soup.children)[16])[1])
  try:
    vals = [re.findall("(?:\d+\.\d+|N/A)", str(list(list(allPrices[2 * i + 1])[1])[0].encode('utf-8')))[0].replace("N/A", "") for i in range(6)]
    print("[{}] on [{}] Has Been Scraped".format(game, console))
    return vals
  except:
    print("[{}] on [{}] Scraping Failed".format(game, console))
    return []

def fill_csv(dt, fn):
  """Creates and fills our csv file

  Args:
    dt: (string) directory name
    fn: (string) filename
  """
  with open(os.path.join(dt, fn), 'w') as csv_file:
    consoles = [console[:len(console) - 4] for console in os.listdir('Games/')]
    fieldnames = ['game', 'console', 'loose_val', 'complete_val', 'new_val', 'graded_val', 'box_val', 'manual_val', 'date(D/M/Y)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    print("[{}] File Created\nFinding {}\n  for {} Consoles\n".format(fn, fieldnames, consoles))
    for console in consoles:
      data = pd.read_csv("Games/" + console + ".csv")
      for game in data['game'].values:
        time.sleep(0.1 + random.randrange(0, 10) * 0.1)
        vals = scrape_pricecharting(console, game)
        if (len(vals) == 6):
          writer.writerow({'game': game.replace('-', ' '), 'console': console, 'loose_val': vals[0], 'complete_val': vals[1], 'new_val': vals[2],
          'graded_val': vals[3], 'box_val': vals[4], 'manual_val': vals[5], 'date(D/M/Y)': dt.split('_')[0].replace('.', '/')})

def create_dir(dt):
  """Creates a new directory in our directory to store our CSV file

  Args:
    dt: (string) directory name
  """
  if not os.path.exists(dt):
    os.mkdir(dt)
    print("Successfully Created Directory [{}]\n".format(dt))

def main():
  """Sets directory name to current data and time, filename to "game_prices.csv" and orders execution of our program
  """
  dt = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
  fn = "game_prices.csv"
  create_dir(dt)
  fill_csv(dt, fn)

def scrape_links(site):
  page = requests.get(site)
  soup = BeautifulSoup(page.content, 'html.parser')
  # allPrices = list(soup)
  for link in soup.findAll('a'):
    print(link.get('href'))


def pull_table():
  urlNes = "https://www.pricecharting.com/console/nes"
  with urllib.request.urlopen(urlNes) as url:
    s = url.read()
    soup = BeautifulSoup(s)
    indicateGameDone = soup.findAll("td", {"class": "price numeric used_price"})
    for x in indicateGameDone:
      print(x.text)




if __name__== "__main__":
  """Entry point for our program
  """
  # pull_table()
  scrape_links("https://www.pricecharting.com/console/nes")
  # site = input("URL")
  # scrape_links(site)
  # main()