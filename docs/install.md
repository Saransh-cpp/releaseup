# Installation

Follow the steps below to install `releaseup` locally.

## Create a virtual environment

Create and activate a virtual environment

```bash
python -m venv env

. env/bin/activate
```

## Install releaseup

- Install Tesseract for your OS and add it to PATH

The installation guide is available
[here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- `pip` magic

`releaseup` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install releaseup
```

## Build releaseup from source

If you want to develop `releaseup`, or use its latest commit (!can be
unstable!), you might want to install it from the source -

- Install Tesseract for your OS and add it to PATH

The installation guide is available
[here](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- Clone this repository

```bash
git clone https://github.com/Saransh-cpp/releaseup
```

- Change directory

```bash
cd releaseup
```

- Install the package in editable mode with the "dev" dependencies

```bash
python -m pip install -e ".[dev]"
```

Feel free to read our
[Contributing Guide](https://github.com/Saransh-cpp/releaseup/blob/main/CONTRIBUTING.md)
for more information on developing `releaseup`.
