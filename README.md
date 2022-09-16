# releaseit

![release_it](https://user-images.githubusercontent.com/74055102/190672849-3d6886d1-558e-41cf-9e6d-a932f7de0997.png)

[![CI](https://github.com/Saransh-cpp/releaseit/actions/workflows/ci.yml/badge.svg)](https://github.com/Saransh-cpp/releaseit/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/release_it/badge/?version=latest)](https://release_it.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Saransh-cpp/releaseit/main.svg)](https://results.pre-commit.ci/latest/github/Saransh-cpp/releaseit/main)
[![codecov](https://codecov.io/gh/Saransh-cpp/releaseit/branch/main/graph/badge.svg?token=L6ObHKhaZ7)](https://codecov.io/gh/Saransh-cpp/releaseit)
[![discussion](https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github)](https://github.com/Saransh-cpp/releaseit/discussions)

[![Python Versions](https://img.shields.io/pypi/pyversions/release_it)](https://pypi.org/project/release_it/)
[![Package Version](https://badge.fury.io/py/release_it.svg)](https://pypi.org/project/release_it/)
[![PyPI Downloads](https://pepy.tech/badge/release_it)](https://pepy.tech/project/release_it)
![License](https://img.shields.io/github/license/Saransh-cpp/releaseit?color=blue)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An extractive `NLP` approach for generating release notes from comments and
docstrings added between two git tags.

`release_it` extracts all the comments and docstrings using `git diff`,
preprocesses the outputs, and finally generates release notes using `sklearn`'s
`TfidfVectorizer` and `spacy`! The generated release notes are not at all
abstractive, which is something `release_it` aims to achieve in the future.

As of now, `release_it` is a holiday project (built in mere 2 days), but I do
intend to maintain it in the future. `release_it` does work, but only if your
comments are well written.

Read more about `release_it` through its
[documentation](https://release_it.readthedocs.io)

## Structure

- All the extraction and preprocessing work is carried out using the `extract`
  module.
- All the extractive `NLP` work is done inside the `nlp_backend` module.
- `release_it` also prvides a high level API present inn the `high_level`
  module.

See [examples](#Examples) for more information.

## Installation

Use `pip` magic

`release_it` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install release_it
```

For developer install, see our
[Contributing Guidelines](https://github.com/Saransh-cpp/releaseit/blob/main/release_it).

## Examples

### High level API

```py
import release_it

tag = ["v0.8.0", "v0.9.0"]  # can also be commits
path = "./src/mypackage/"  # to ignore changes made to other folders (./github/, docs/, etc) and files
comments_filename = "COMMENTS.txt"

# extract added comments and docstrings
comments = release_it.extract_release_comments(
    tags, path, comments_filename
)

release_filename = "RELEASE_NOTES.txt"

# generate release notes
notes = release_it.generate_release_notes(
    comments,
    release_filename,
    model_name = "en_core_web_trf",  # any spacy model
    threshold = 0.3,  # percentage of comments to be selected
)
```

### Low level API

```py
from release_it.extract import (
    extract_additions,
    get_comments_and_docstrings,
    get_diff,
    preprocess_additions,
)
from release_it.nlp_backend import get_release_notes, get_tfid_scores

tag = ["v0.8.0", "v0.9.0"]  # can also be commits
path = "./src/mypackage/"  # to ignore changes made to other folders (./github/, docs/, etc) and files
comments_filename = "COMMENTS.txt"

# extract added comments and docstrings
get_diff(tags, path, comments_filename)
extracted_additions = extract_additions(comments_filename)
preprocessed_additions = preprocess_additions(extracted_additions)
comments = get_comments_and_docstrings(preprocessed_additions)

release_filename = "RELEASE_NOTES.txt"

word_score = get_tfid_scores(comments)
release_notes = get_release_notes(
    comments,
    word_score,
    release_filename,
    model_name = "en_core_web_trf",  # any spacy model
    threshold = 0.3,  # percentage of comments to be selected
)
```

## Testing

**TODO: ADD TESTS**

## Activating pre-commit

`release_it` uses a set of `pre-commit` hooks and the `pre-commit` bot to
format, type-check, and prettify the codebase. The hooks can be installed
locally using -

```
pre-commit install
```

This would run the checks every time a commit is created locally. The checks
will only run on the files modified by that commit, but the checks can be
triggered for all the files using -

```
pre-commit run --all-files
```

If you would like to skip the failing checks and push the code for further
discussion, use the `--no-verify` option with `git commit`.

## Documenting release_it

`release_it`'s documentation is mainly written in the form of
[docstrings](https://peps.python.org/pep-0257/) and
[Markdown](https://en.wikipedia.org/wiki/Markdown). The docstrings include the
description, arguments, examples, return values, and attributes of a class or a
function, and the `.md` files enable us to render this documentation on
`release_it`'s documentation website.

`release_it` primarily uses [MkDocs](https://www.mkdocs.org/) and
[mkdocstrings](https://mkdocstrings.github.io/) for rendering documentation on
its website. The configuration file (`mkdocs.yml`) for `MkDocs` can be found
[here](https://github.com/Saransh-cpp/releaseit/blob/main/mkdocs.yml). The
documentation is deployed on <https://readthedocs.io>
[here](https://release_it.readthedocs.io/en/latest/).

Ideally, with the addition of every new feature to `release_it`, documentation
should be added using comments, docstrings, and `.md` files.

### Building documentation locally

The documentation is located in the `docs` folder of the main repository. This
documentation can be generated using the `docs` dependencies of `release_it` in
the following way -

```
mkdocs serve
```

The commands executed above will clean any existing documentation build, create
a new build (in `./site/`), and serve it on your `localhost`. To just build the
documentation, use -

```
mkdocs build
```

## Nox

The fastest way to start with development is to use nox. If you don't have nox,
you can use `pipx run nox` to run it without installing, or `pipx install nox`.
If you don't have pipx (pip for applications), then you can install with with
`pip install pipx` (the only case were installing an application with regular
pip is reasonable). If you use macOS, then pipx and nox are both in brew, use
`brew install pipx nox`.

To use, run `nox`. This will lint and test using every installed version of
Python on your system, skipping ones that are not installed. You can also run
specific jobs:

```console
$ nox -s lint  # Lint only
$ nox -s tests-3.9  # Python 3.9 tests only
$ nox -s docs -- serve  # Build and serve the docs
$ nox -s build  # Make an SDist and wheel
```

The default sessions (`lint` and `tests`) can be executed using -

```
nox
```

## Continuous Integration

`release_it` uses `GitHub Actions` as a `CI` provider to run tests, build docs,
release on `PyPI`, test package, etc. All the configuration for `GitHub Actions`
is written in `YAML`, present in `.github/` directory. The CI runs every time a
pull request is made or a push is made to the `main` branch.

## Continuous Deployment

`release_it` uses `Read The Docs` as a `CD` provider to deploy documentation.
All the configuration for `Read The Docs` is written in `YAML`, present in the
`.readthedocs.yml` file. The CD runs every time a push is made to the `main`
branch.

## Credits

Logo image credits: Taufik Ramadhan (taken from canva)
