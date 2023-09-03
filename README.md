# releaseup

![releaseup](https://user-images.githubusercontent.com/74055102/190684416-d3f15189-8c4f-4a11-a374-500e8496d9b1.png)

[![CI](https://github.com/Saransh-cpp/releaseup/actions/workflows/ci.yml/badge.svg)](https://github.com/Saransh-cpp/releaseup/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/releaseup/badge/?version=latest)](https://releaseup.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Saransh-cpp/releaseup/main.svg)](https://results.pre-commit.ci/latest/github/Saransh-cpp/releaseup/main)
[![codecov](https://codecov.io/gh/Saransh-cpp/releaseup/branch/main/graph/badge.svg?token=L6ObHKhaZ7)](https://codecov.io/gh/Saransh-cpp/releaseup)
[![discussion](https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github)](https://github.com/Saransh-cpp/releaseup/discussions)

[![Python Versions](https://img.shields.io/pypi/pyversions/releaseup)](https://pypi.org/project/releaseup/)
[![Package Version](https://badge.fury.io/py/releaseup.svg)](https://pypi.org/project/releaseup/)
[![Downloads](https://static.pepy.tech/badge/releaseup)](https://pepy.tech/project/releaseup)
![License](https://img.shields.io/github/license/Saransh-cpp/releaseup?color=blue)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An extractive `NLP` approach for generating release notes from comments and
docstrings added between two git tags.

`releaseup` extracts all the comments and docstrings using `git diff`,
preprocesses the outputs, and finally generates release notes using `sklearn`'s
`TfidfVectorizer` and `spacy`! The generated release notes are not at all
abstractive, which is something `releaseup` aims to achieve in the future.

As of now, `releaseup` is a holiday project (built in mere 2 days), but I do
intend to maintain it in the future. `releaseup` does work, but only if your
comments are well written.

Read more about `releaseup` through its
[documentation](https://releaseup.readthedocs.io).

## Structure

- All the extraction and preprocessing work is carried out using the `extract`
  module.
- All the extractive `NLP` work is done inside the `nlp_backend` module.
- `releaseup` also prvides a high level API present inn the `high_level` module.

See [examples](#Examples) for more information.

## Installation

Use `pip` magic

`releaseup` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install releaseup
```

For developer install, see our
[Contributing Guidelines](https://github.com/Saransh-cpp/releaseup/blob/main/releaseup).

## Examples

### High level API

```py
import releaseup

tag = ["v0.8.0", "v0.9.0"]  # can also be commits
path = "././mypackage/"  # to ignore changes made to other folders (./github/, docs/, etc) and files
comments_filename = "COMMENTS.txt"

# extract added comments and docstrings
comments = releaseup.extract_release_comments(tags, path, comments_filename)

release_filename = "RELEASE_NOTES.txt"

# generate release notes
notes = releaseup.generate_release_notes(
    comments,
    release_filename,
    model_name="en_core_web_trf",  # any spacy model
    threshold=0.3,  # percentage of comments to be selected
)
```

### Low level API

```py
from releaseup.extract import (
    extract_additions,
    get_comments_and_docstrings,
    get_diff,
    preprocess_additions,
)
from releaseup.nlp_backend import get_release_notes, get_tfid_scores

tag = ["v0.8.0", "v0.9.0"]  # can also be commits
path = "././mypackage/"  # to ignore changes made to other folders (./github/, docs/, etc) and files
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
    model_name="en_core_web_trf",  # any spacy model
    threshold=0.3,  # percentage of comments to be selected
)
```

## Testing

**TODO: ADD TESTS**

## Activating pre-commit

`releaseup` uses a set of `pre-commit` hooks and the `pre-commit` bot to format,
type-check, and prettify the codebase. The hooks can be installed locally
using -

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

## Documenting releaseup

`releaseup`'s documentation is mainly written in the form of
[docstrings](https://peps.python.org/pep-0257/) and
[Markdown](https://en.wikipedia.org/wiki/Markdown). The docstrings include the
description, arguments, examples, return values, and attributes of a class or a
function, and the `.md` files enable us to render this documentation on
`releaseup`'s documentation website.

`releaseup` primarily uses [MkDocs](https://www.mkdocs.org/) and
[mkdocstrings](https://mkdocstrings.github.io/) for rendering documentation on
its website. The configuration file (`mkdocs.yml`) for `MkDocs` can be found
[here](https://github.com/Saransh-cpp/releaseup/blob/main/mkdocs.yml). The
documentation is deployed on <https://readthedocs.io>
[here](https://releaseup.readthedocs.io/en/latest/).

Ideally, with the addition of every new feature to `releaseup`, documentation
should be added using comments, docstrings, and `.md` files.

### Building documentation locally

The documentation is located in the `docs` folder of the main repository. This
documentation can be generated using the `docs` dependencies of `releaseup` in
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

`releaseup` uses `GitHub Actions` as a `CI` provider to run tests, build docs,
release on `PyPI`, test package, etc. All the configuration for `GitHub Actions`
is written in `YAML`, present in `.github/` directory. The CI runs every time a
pull request is made or a push is made to the `main` branch.

## Continuous Deployment

`releaseup` uses `Read The Docs` as a `CD` provider to deploy documentation. All
the configuration for `Read The Docs` is written in `YAML`, present in the
`.readthedocs.yml` file. The CD runs every time a push is made to the `main`
branch.

## Credits

Logo image credits: Taufik Ramadhan (taken from canva)
