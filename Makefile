install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest .

format:
	black .

lint:
	pylint .

refactor: format lint test

