install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest .

format:
	black search_engine_comparison.py

lint:
	pylint .

refactor: format lint test

