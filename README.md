# Pricecharting Scraper

> Uses web scraping to pull loose, CIB, and new market values for video games from pricecharting.com and outputs them to a CSV file.

## Requirements

- Python 3.8+
- Google Chrome installed

On WSL/Ubuntu:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

## Setup

MacOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python3 scraper.py [--console CONSOLE] [--output FILENAME] [--workers N] [--pause SECONDS]
```

### Arguments

| Argument    | Default           | Description                                                                           |
| ----------- | ----------------- | ------------------------------------------------------------------------------------- |
| `--console` | _(all consoles)_  | Scrape a single console by slug (e.g. `super-nintendo`). Omit to scrape all consoles. |
| `--output`  | `game_prices.csv` | Output CSV filename                                                                   |
| `--workers` | `1`               | Number of concurrent browser instances. See note below before increasing.             |
| `--pause`   | `1.5`             | Seconds to wait between scroll attempts. Increase if games are not fully loading.     |

### Examples

```bash
# Scrape all consoles, output to default file
python3 scraper.py

# Scrape a single console
python3 scraper.py --console super-nintendo

# Scrape a single console to a custom file
python3 scraper.py --console nintendo-64 --output n64_prices.csv

# Scrape all consoles with a custom output file
python3 scraper.py --output full_catalog.csv

# Increase scroll pause time (useful if games aren't fully loading)
python3 scraper.py --console nes --pause 3.0
```

### A note on `--workers`

By default the scraper runs one console at a time. You can increase `--workers` to scrape multiple consoles concurrently, but be aware:

- Each worker spawns a full headless Chrome instance. On WSL, RAM is limited and multiple Chrome instances compete for CPU.
- Under high CPU load, the page's lazy-loading may not fire within the pause window, resulting in only the first ~100 games being scraped per console.
- If you increase workers, also increase `--pause` to compensate (e.g. `--workers 3 --pause 3.0`).

## Consoles Scraped

By default, all major NTSC consoles are scraped:

**Nintendo:** NES, SNES, N64, GameCube, Wii, Wii U, Switch, Switch 2, Game Boy, Game Boy Color, Game Boy Advance, DS, 3DS, Virtual Boy, Game & Watch

**Sony:** PlayStation, PS2, PS3, PS4, PS5, PSP, PS Vita

**Microsoft:** Xbox, Xbox 360, Xbox One, Xbox Series X

**Sega:** Master System, Genesis, 32X, CD, Saturn, Dreamcast, Game Gear, Pico

**Atari:** 2600, 5200, 7800, 400, Lynx, Jaguar

**SNK:** Neo Geo MVS, Neo Geo AES, Neo Geo CD, Neo Geo Pocket Color

## CSV Format

| Column         | Description                          |
| -------------- | ------------------------------------ |
| `game`         | Game title                           |
| `console`      | Console slug (e.g. `super-nintendo`) |
| `loose_val`    | Loose / cartridge-only price         |
| `complete_val` | Complete in box (CIB) price          |
| `new_val`      | New/sealed price                     |
| `date(D/M/Y)`  | Date the data was scraped            |

## Known Limitations

- **WSL concurrency** — Running multiple workers (`--workers > 1`) on WSL can cause Chrome to crash or pages to load incompletely due to CPU and memory contention. If you see only ~100 games scraped per console, try reducing to `--workers 1` and increasing `--pause` to `2.5` or higher.
- **Apple Silicon (M1/M2/M3)** — `webdriver-manager` may download an incorrect ChromeDriver binary on ARM Macs. If Chrome fails to launch, install Chrome manually and use Selenium's built-in driver manager by removing the `Service(ChromeDriverManager().install())` call and passing only `options` to `webdriver.Chrome()`.
- **Site changes** — This scraper targets specific HTML element IDs and CSS classes on pricecharting.com. If the site updates its layout, the scraper may stop returning data or return incomplete results. If you encounter this, please [open an issue](https://github.com/markfoster314/Pricecharting-Scraper/issues/new).
- **Rate limiting** — No request throttling is implemented between consoles. Running many workers simultaneously may result in your IP being temporarily rate-limited by pricecharting.com.
- **N/A prices** — Some games do not have a listed price for all three conditions (loose, CIB, new). These are recorded as `N/A` in the CSV.

## Disclaimer

This project is intended for personal and educational use only. It is not affiliated with, endorsed by, or connected to [PriceCharting.com](https://www.pricecharting.com) in any way. If you need programmatic access to their data at scale, consider using their [official API](https://www.pricecharting.com/api-documentation).
Please use this tool responsibly and in accordance with PriceCharting's [terms of service](https://www.pricecharting.com/page/terms-of-service).
