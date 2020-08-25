venv:
	python3 -m venv venv

update:
	pip3 install -r requirements.txt

update_with_pip:
	pip install -r requirements.txt

run:
	python3 -m Problem2.qualifying_offer