# Installation

Follow the steps below to install `release_it` locally.

## Create a virtual environment

Create and activate a virtual environment

```bash
python -m venv env

. env/bin/activate
```

## Install release_it

- Install Tesseract for your OS and add it to PATH

The installation guide is available
[here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- `pip` magic

`release_it` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install release_it
```

## Build release_it from source

If you want to develop `release_it`, or use its latest commit (!can be
unstable!), you might want to install it from the source -

- Install Tesseract for your OS and add it to PATH

The installation guide is available
[here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- Clone this repository

```bash
git clone https://github.com/Saransh-cpp/release_it
```

- Change directory

```bash
cd release_it
```

- Install the package in editable mode with the "dev" dependencies

```bash
python -m pip install -e ".[dev]"
```

Feel free to read our
[Contributing Guide](https://github.com/Saransh-cpp/release_it/blob/main/CONTRIBUTING.md)
for more information on developing `release_it`.
