# Probabilistic Modeling of Student Success: A Bayesian Network Analysis of Behavioral Determinants

## Setup (Assuming you have Python3 installed)

```bash
git clone https://github.com/mahirpatel04/cse150a_final_project.git
cd cse150a_final_project
make setup
```

This will:

- Create a virtual environment (`.venv`)
- Install dependencies from `requirements.txt`
- Download and extract the dataset to `data/`

## Setup (If you are using Window)

### install Python 3.10+ and Git

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/install/windows)

### install Make + unzip using MSYS2

- [MSYS2](https://www.msys2.org/)

- Open MSYS2 MinGW 64-bit terminal and run:

```bash
pacman -Syu
pacman -Sy make unzip
```

- Add the following to your local System PATH:

```bash
C:\msys64\usr\bin
C:\msys64\mingw64\bin
```

- Restart the VS code

### After cloning the project 
- First make sure your Makefile have a proper path by:
```bash
make --version
```

- Create Virtual Env
```bash
python -m venv .venv
```

- Verify that .venv/Scripts contains:
  - python.exe
  - pip. exe

### Install Kaggle CLI inside venv

```bash
.venv/Scripts/pip install --force-reinstall kaggle
```

you should see kaggle.exe inside the .venv/Scripts

### Ready to go

```bash
make setup
```
