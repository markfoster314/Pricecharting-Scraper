.PHONY: venv install run clean

venv:
	python3 -m venv venv

install: venv
	./venv/bin/pip install -r requirements.txt

run:
	./venv/bin/python scraper.py

clean:
	rm -rf venv __pycache__
