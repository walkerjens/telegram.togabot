PYTHON=python3
PIP=pip3

.PHONY: venv install

venv:
	$(PYTHON) -m venv venv
	. venv/bin/activate

install:
	$(PIP) install -r requirements.txt
