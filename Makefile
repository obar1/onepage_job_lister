install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest search_engine_comparison.py

format:
	black search_engine_comparison.py

lint:
	pylint search_engine_comparison.py

refactor: format lint test

