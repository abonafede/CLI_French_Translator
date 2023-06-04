setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	python3 setup.py develop

lint: 
	pylint --disable=R,C translator.py

format:
	black translator.py translator_test.py

test:
	python3 -m pytest -vv --cov=translator_test.py

all: setup lint format test