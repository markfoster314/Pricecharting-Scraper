# Pricecharting Scraper
> This program uses web scraping to pull market values for video games from Pricecharting.com without purchasing their API

Pricecharting takes completed eBay transactions for classic video games over the past three months, and averages their prices to come up with fair market values. They sell an API to query this data, but the information is also available online for free, and listed plainly in their HTML. This application uses web scraping to create CSV files with these video games' fair market values.

## Installation

### Required

- `scraper.py` and a `Games` directory in the same directory
- CSV files inside of the `Games` directory specifying which games to query
> NOTE: For the time being, each console must have its own csv file, `[console].csv`, where `console` is the console's name as it appears on pricecharting's URL. Each csv file must contain one column, `game`, which stores a list of games to be queried for that console in the format of pricecharting's URL. This will be changed in a future update

### Clone

- Clone this repo to your local machine using `https://github.com/markfoster314/Pricecharting-Scraper`

## Usage examples

Using eBay's APIs, you can query active listings for these video games, compare their price to the values in the filled CSV files, and set up an application to notify you whenever there's a great deal.

Run this script daily to gather historical pricing information for these video games, then come up with future price predictions and invest in video games

## Meta

Mark Foster – [LinkedIn](https://www.linkedin.com/in/markfoster314/) – markfoster314@yahoo.com


<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
