# Pricecharting Scraper

> A Python-based web scraper that collects fair market values for video games from [PriceCharting.com](https://www.pricecharting.com), without requiring a paid API subscription.

PriceCharting uses eBay's transaction data to calculate fair market values for video games across three conditions: **loose** (cartridge only), **complete in box** (cartridge + manual + box), and **sealed/new**. While they offer a paid API, this data is also freely available on their website. This scraper automates the collection of that data into structured CSV output.

---

## Getting Started

### Prerequisites

- Python 3.4+
- Firefox browser — [Download here](https://www.mozilla.org/en-US/firefox/new/) if not already installed
- `geckodriver` — required by Selenium to drive Firefox; see [installation instructions](https://selenium.dev/selenium/docs/api/py/)

### Clone the Repository

```bash
git clone https://github.com/slongstreet/Pricecharting-Scraper.git
cd Pricecharting-Scraper
```

### Install Dependencies

This project uses a Python virtual environment managed via `make`:

```bash
make install
```

This creates a `venv/` directory and installs all packages from `requirements.txt`.

---

## Usage

### Run the Scraper

```bash
make run
```

This executes `scraper.py` using the project's virtual environment. The scraper will open Firefox, scroll through the PriceCharting page for each configured console, and collect pricing data.

### Output

After a successful run, two outputs are generated:

- **Timestamped folder** (e.g., `14.03.2026_12.00.00/`) — contains `game_prices.csv` with the scraped data for that run.
- **`output-latest/`** — always contains the most recent run's `game_prices.csv` and a `manifest.json` with the corresponding datestamp.

### Initialize the Database

```bash
make db
```

Runs `create_db.py` to initialize a local SQLite database (`gameprices.db`).

### Clean the Project

```bash
make clean
```

Removes the virtual environment (`venv/`), Python cache, and any timestamped output directories.

---

## Configuration

To change which consoles are scraped, edit the `CONSOLES` list near the top of `scraper.py`:

```python
CONSOLES = ["sega-game-gear"]
```

Console names must match their URL slug on PriceCharting (e.g., `"super-nintendo"`, `"nintendo-64"`, `"playstation-2"`). A larger commented-out list of supported consoles is included in the file for reference.

---

## Use Cases

- **Deal hunting** — Compare scraped prices against active eBay listings to surface great deals automatically.
- **Price history** — Run the scraper on a schedule to build a historical pricing dataset for trend analysis.
- **Investment research** — Track value changes over time to inform video game collecting decisions.

---

## Acknowledgements

This project is a fork of the original [Pricecharting-Scraper](https://github.com/markfoster314/Pricecharting-Scraper) by [Mark Foster](https://github.com/markfoster314). Thanks to Mark for the initial implementation.