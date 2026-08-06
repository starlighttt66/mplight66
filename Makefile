VENV := .venv
PY := $(VENV)/bin/python3

.PHONY: venv prep run

venv:
	python3 -m venv $(VENV)

prep: venv
	$(PY) -m pip install -U pip
	$(PY) -m pip install -r requirements.txt

run: prep
	$(PY) ui.py