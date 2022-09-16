# Contributing guide

If you are planning to develop `releaseup`, or want to use the latest commit of
`releaseup` on your local machine, you might want to install it from the source.
This installation is not recommended for users who want to use the stable
version of `releaseup`. The steps below describe the installation process of
`releaseup`'s latest commit. It also describes how to test `releaseup`'s
codebase and build `releaseup`'s documentation.

**Note**: `releaseup` uses
[Scikit-HEP's developer information](https://scikit-hep.org/developer) as a
reference for all the development work. The guide is a general and much more
explained collection of documentation available for developing `Scikit-HEP`
packages. `releaseup` is not a `Scikit-HEP` package, but it still loosely
follows this developer guide as it is absolutely amazing!

## Installing releaseup

We recommend using a virtual environment to install `releaseup`. This would
isolate the library from your global `Python` environment, which would be
beneficial for reproducing bugs, and the overall development of `releaseup`. The
first step would be to clone `releaseup` -

```
git clone https://github.com/Saransh-cpp/releaseup.git
```

and then we can change the current working directory and enter `releaseup` -

```
cd releaseup
```

### Creating a virtual environment

A virtual environment can be set up and activated using `venv` in both `UNIX`
and `Windows` systems.

**UNIX**:

```
python3 -m venv .env
. .env/bin/activate
```

**Windows**:

```
python -m venv .env
.env\bin\activate
```

### Installation

The developer installation of `releaseup` comes with a lot of options -

- `test`: the test dependencies
- `docs`: extra dependencies to build and develop `releaseup`'s documentation
- `dev`: installs the `test` and `docs` dependencies

These options can be used with `pip` with the editable (`-e`) mode of
installation in the following ways -

```
pip install -e .[dev,test]
```

For example, if you want to install the `docs` dependencies along with the
dependencies included above, use -

```
pip install -e .[dev,test,docs]
```

### Adding releaseup for notebooks

`releaseup` can be added to the notebooks using the following commands -

```
python -m ipykernel install --user --name releaseup
```

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

## Testing

**TODO: ADD TESTS**

### Running tests with coverage locally

The coverage value can be obtained while running the tests using `pytest-cov` in
the following way -

```
python -m pytest -ra --cov=releaseup tests/
```

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

### Running pre-commit with nox

The `pre-commit` hooks can be run with `nox` in the following way -

```
nox -s lint
nox -s pylint
```

### Running tests with nox

Tests can be run with `nox` in the following way -

```
nox -s tests
```

### Building documentation with nox

Docs can be built with `nox` in the following way -

```
nox -s docs
```

Use the following command if you want to deploy the docs on `localhost` -

```
nox -s docs -- serve
```
