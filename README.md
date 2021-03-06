# Pricecharting Scraper
> This program uses web scraping to pull market values for video games from Pricecharting.com without purchasing their API

Pricecharting uses eBay's APIs to query successful transactions over the past three months for video games, classifies each transaction, then averages these values to come up with fair market values for loose cartridges, complete in box games (cartridge + manual + box), and sealed games. They sell an API to query this data, but the information is also available online for free. This application uses web scraping to create a CSV file with games' fair market values.

## Installation

### Required
- Python 3.4+
- Firefox browser
  - Currently working on support for Chrome, Edge and Safari
  - In the meantime if Firefox is not installed on your machine install it [here](https://www.mozilla.org/en-US/firefox/new/)
- Selenium and geckodriver
  - This application uses Selenium for web based automation which requires geckodriver for use in Firefox.
  - Click [here](https://selenium.dev/selenium/docs/api/py/) for installation instructions

### Clone

- Clone this repo to your local machine using `https://github.com/markfoster314/Pricecharting-Scraper`

## Run
- To run this application, ensure all dependencies are fulfilled, navigate to your directory,  and run `scraper.py`
- If run correctly, a new directory titled with the current date and time should be created in your directory. This directory contains a csv file `game_prices.csv` which contains all the scraped data

## Usage examples

Using eBay's APIs, you can query active listings for these video games, compare their price to the values in the filled CSV files, and set up an application to notify you whenever there's a great deal.

Run this script daily to gather historical pricing information for these video games, then come up with future price predictions and invest in video games

## Meta

Mark Foster – [LinkedIn](https://www.linkedin.com/in/markfoster314/) – markfoster314@yahoo.com