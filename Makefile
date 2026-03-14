.PHONY: install run clean

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

install: venv/bin/activate

run: venv/bin/activate
	./venv/bin/python scraper.py

clean:
	rm -rf venv __pycache__ [0-9][0-9].[0-9][0-9].[0-9][0-9][0-9][0-9]_[0-9][0-9].[0-9][0-9].[0-9][0-9]
