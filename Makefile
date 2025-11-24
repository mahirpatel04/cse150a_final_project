.PHONY: setup install download-data clean

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

setup: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Setup complete!"

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

download-data: $(VENV)
	@mkdir -p data
	$(VENV)/bin/kaggle datasets download kainatjamil12/students-exams-score-analysis-dataset -p data
	@echo "Data downloaded to data/ folder"

clean:
	rm -rf $(VENV)
	rm -rf data/*.zip
	@echo "Cleaned virtual environment and downloaded data files"
