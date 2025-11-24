.PHONY: setup install download-data clean

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

setup: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(MAKE) download-data
	@echo "Setup complete!"

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

download-data:
	@mkdir -p data
	@if [ -f $(VENV)/bin/kaggle ]; then \
		$(VENV)/bin/kaggle datasets download kainatjamil12/students-exams-score-analysis-dataset -p data; \
	else \
		kaggle datasets download kainatjamil12/students-exams-score-analysis-dataset -p data; \
	fi
	@if [ -f data/students-exams-score-analysis-dataset.zip ]; then \
		unzip -o data/students-exams-score-analysis-dataset.zip -d data; \
		rm -f data/students-exams-score-analysis-dataset.zip; \
		echo "Data extracted to data/ folder"; \
	fi
	@echo "Data downloaded and extracted to data/ folder"

clean:
	rm -rf $(VENV)
	rm -rf data/*.zip
	@echo "Cleaned virtual environment and downloaded data files"
