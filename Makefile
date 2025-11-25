# Detect OS (Windows)
ifeq ($(OS), Windows_NT)
    PYTHON = .venv/Scripts/python.exe
    PIP = .venv/Scripts/pip.exe
    KAGGLE = .venv/Scripts/kaggle.exe
else
    PYTHON = .venv/bin/python3
    PIP = .venv/bin/pip
    KAGGLE = .venv/bin/kaggle
endif

.PHONY: setup install download-data clean

# Setup
setup: $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	$(MAKE) download-data
	@echo "Setup complete!"

# Create virtual environment
$(VENV):
	# Windows uses python, macOS uses python3
ifeq ($(OS), Windows_NT)
	python -m venv .venv
else
	python3 -m venv .venv
endif

# Download + extract dataset
download-data:
	@mkdir -p data
	$(KAGGLE) datasets download kainatjamil12/students-exams-score-analysis-dataset -p data

	@if [ -f data/students-exams-score-analysis-dataset.zip ]; then \
		unzip -o data/students-exams-score-analysis-dataset.zip -d data; \
		rm -f data/students-exams-score-analysis-dataset.zip; \
		echo "Data extracted to data/ folder"; \
	fi

	@echo "Data downloaded and extracted to data/ folder"

clean:
	rm -rf .venv
	rm -rf data/*.zip