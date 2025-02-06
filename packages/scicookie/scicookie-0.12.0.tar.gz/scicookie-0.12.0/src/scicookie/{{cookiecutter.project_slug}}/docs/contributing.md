# Contributing

In order to be able to contribute, it is important that you understand the
project layout.

{% if cookiecutter.project_layout == "src" -%}
This project uses the _src layout_, which means that the package code is located
at `./src/{{ cookiecutter.package_slug }}`.
{% else -%}
This project uses the _flat layout_, which means that the package code is located
at `./{{ cookiecutter.package_slug }}`.
{% endif %}
For my information, check the official documentation:
<https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>

{% if cookiecutter.build_system == "poetry" -%}
In addition, you should know that to build our package we use
[Poetry](https://python-poetry.org/), it's a Python package management tool
that simplifies the process of building and publishing Python packages. It
allows us to easily manage dependencies, virtual environments and package
versions. Poetry also includes features such as dependency resolution, lock
files and publishing to PyPI. Overall, Poetry streamlines the process of
managing Python packages, making it easier for us to create and share our code
with others.
{%- elif cookiecutter.build_system == "flit" -%}
In addition, you should know that to build our package we use
[Flit](https://flit.pypa.io), it's a Python package that simplifies the process
of publishing Python packages. It allows us to easily create and publish our
packages to PyPI. Flit handles the packaging, distribution, and installation of
Python packages, making it easier for us to share our code with others. It also
includes features such as dependency management, versioning, and metadata
management.
{%- elif cookiecutter.build_system == "mesonpy" -%}
In addition, you should know that to build our package we use
[meson-python](https://meson-python.readthedocs.io/en/latest/index.html), it's
a tool for automating and simplifying the construction of software projects
written in the Python programming language. It is based on the _Meson_ build
system, which allows you to efficiently configure and manage the build process
of a project. It allows you to easily define project dependencies, specify
build options, generate configuration files and build scripts, among other
tasks related to building software.
{%- elif cookiecutter.build_system == "setuptools" -%}
In addition, you should know that to build our package we use
[Setuptools](https://setuptools.pypa.io/en/latest/), it's a package to easily
define the package structure, manage dependencies and co nvert our project into
a distributable package. Also, setuptools automates tasks such as packaging and
installation, saving time and effort for both our team and end-users.
{%- elif cookiecutter.build_system == "pdm" -%}
In addition, you should know that to build our package we use
[PDM](https://pdm.fming.dev/), it's a build system for Python projects. It
provides an efficient and fast way to manage project dependencies, as well as
build and distribute code. It is fast to install, has built-in virtualenv,
offers support for different package sources, and provides an easy way to
distribute code.
{%- elif cookiecutter.build_system == "pixi" -%}
In addition, you should know that to build our package we use
[Pixi](https://pixi.sh/latest/), it's a package management tool for developers.
It allows the developer to install libraries and applications in a reproducible
way. Use pixi cross-platform, on Windows, Mac and Linux.
{%- elif cookiecutter.build_system == "hatch" -%}
In addition, you should know that to build our package we use
[Hatch](https://hatch.pypa.io): It's a Python Package that is compatible build
backend used by Hatch, a modern, extensible Python project manager. It provides
a standardized build system with reproducible builds by default, robust
environment management with support for custom scripts, easy publishing to PyPI
or other indexes, version management, and configurable project generation with
sane defaults. Hatchling might support multiple programming languages and offer
language-specific options for building projects in different languages. It
could also provide customization and extensibility options, allowing you to
incorporate plugins or scripts for tailored build processes.
{%- elif cookiecutter.build_system == "maturin" -%}
In addition, you should know that to build our package we use
[Maturin](https://pypi.org/project/maturin/0.8.2/): It's a Python packaging
tool and build system for creating Python bindings from Rust projects. It
enables seamless integration of Rust code into Python applications, offering
efficient builds, cross-platform support, and compatibility with different
Python versions. Maturin automates the process of generating Python modules
that directly call Rust functions, leveraging Rust's performance and low-level
capabilities in Python. With its easy-to-use interface and integration with
setuptools and Cargo, Maturin provides a straightforward solution for
developers seeking to combine the strengths of Python and Rust in a single
project.
{%- elif cookiecutter.build_system == "scikit-build-core" -%}
In addition, you should know that to build our package we use
[scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/): It's
a Python packaging tool and build system an improved build system generator for
CPython C extensions. It provides better support for additional compilers,
build systems, cross compilation, and locating dependencies and their
associated build requirements.This tool improves package management in the
scientific Python ecosystem, enabling cross-platform builds with CMake, and
seamless integration with C/C++ libraries for research software engineers.
{%- elif cookiecutter.build_system == "pybind11" -%}
In addition, you should know that to build our package we use [setuptools +
pybind11](https://pybind11.readthedocs.io/en/stable/): It's a Python packaging
tool for C++ build system that simplifies creating Python bindings for C++
code, allowing easy integration of C++ functions and classes into Python
scripts. Acting as a bridge between the two languages, it enables direct calls
to C++ functionality from Python as if it were a native Python module. Its
user-friendly syntax reduces boilerplate code, while standard C++ build systems
like CMake or Make aid in project compilation. Pybind11's efficiency and strong
community support make it a popular choice for projects requiring seamless
interoperability between C++ and Python, from scientific computing to game
development.

{%- endif %}

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at {{ cookiecutter.git_https_upstream }}/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with “bug” and “help
wanted” is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with “enhancement”
and “help wanted” is open to whoever wants to implement it.

### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog
posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at {{ cookiecutter.git_https_upstream }}/issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are
  welcome :)

## Get Started

Ready to contribute? Here’s how to set up `{{ cookiecutter.project_slug }}` for local
development.

1. Fork the `{{ cookiecutter.project_slug }}` repo on GitHub.
2. Clone your fork locally and change to the directory of your project:

```bash
$ git clone git@github.com:your_name_here/{{ cookiecutter.project_slug }}.git
$ cd {{cookiecutter.project_slug }}/
```

{% if cookiecutter.git_https_upstream -%}
Also, create a remote to the upstream repository, you will need that later:

```bash
$ git remote add upstream {{ cookiecutter.git_https_upstream }}
$ git fetch --all
```

{% endif -%}

### Prepare and use virtual environment

{%- if cookiecutter.use_conda == "yes" %}
If you don't have yet conda installed in your machine, you can check the
installation steps here:
<https://github.com/conda-forge/miniforge?tab=readme-ov-file#download>
After that, ensure that conda is already available in your terminal session and
run:

```bash
$ conda env create env create --file conda/dev.yaml
$ conda activate {{ cookiecutter.package_slug }}
```

Note: you can use `mamba env create` instead, if you have it already installed,
in order to boost the installation step.
{% elif cookiecutter.use_pyenv == "yes" -%}
Create your environment using `virtualenv`:

```bash
$ virtualenv {{ cookiecutter.package_slug }}
$ source {{ cookiecutter.package_slug }}/bin/activate
```

{% else -%}
We highly recommend you to use `conda` for managing virtual environment, but
you can use any other one of your preference.
{% endif -%}

### Install the dependencies

Now, you can already install the dependencies for the project:

{% if cookiecutter.build_system == "poetry" -%}

```bash
$ poetry install
```

{%- elif cookiecutter.build_system == "pdm" -%}

```bash
$ pdm install
```

{%- elif cookiecutter.build_system == "flit" -%}

```bash
$ flit install
```
{%- elif cookiecutter.build_system == "pixi" -%}

```bash
$ pixi install
```

{%- else -%}

```bash
$ pip install -e ".[dev]"
```

{%- endif -%}

### Create a Development Branch

Make a dedicated branch for your bugfix or feature.

```bash
$ git checkout -b name-of-your-bugfix-or-feature
```

### Make Changes Locally

You are now ready to implement your changes or improvements.

{% if cookiecutter.use_pre_commit == "yes" %}

### Install and Use Pre-commit Hooks

- `{{ cookiecutter.project_slug }}` uses a set of `pre-commit` hooks to
improve code quality. The hooks can be installed locally using:

```bash
$ pre-commit install
```

This would run the checks every time a `git commit` is executed locally.
Usually, the verification will only run on the files modified by that commit,
but the verification can also be triggered for all the files using:

```bash
$ pre-commit run --all-files
```

If you would like to skip the failing checks and push the code for further
discussion, use the `--no-verify` option with `git commit`.
{% endif -%}
{% if cookiecutter.use_pytest == "yes" %}

### Unit Testing with `pytest`

This project uses `pytest` as a testing tool. `pytest` is responsible for
testing the code, whose configuration is available in pyproject.toml.
Additionally, this project also uses `pytest-cov` to calculate the coverage of
these unit tests. For more information, check the section about tests later in
this document.
{% elif cookiecutter.use_hypothesis == "yes" %}

### Testing with `hypothesis`

This project uses `hypothesis` as a testing tool. For more information,
please check its official documentation <https://hypothesis.readthedocs.io/>
{% endif %}

### Commit your changes and push your branch to GitHub

```bash
$ git add .
$ git commit -m "Your detailed description of your changes.""
$ git push origin name-of-your-bugfix-or-feature
```

- Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
    new functionality into a function with a docstring, and add the feature to
    the list in README.rst.
3. The pull request should work for Python >= 3.8.

{% if cookiecutter.use_pytest == "yes" -%}

## Running tests locally

The tests can be executed using the `test` dependencies of
`{{ cookiecutter.project_slug }}` in the following way:

```bash
$ python -m pytest
```

{% if cookiecutter.use_coverage == "yes" -%}

### Running tests with coverage locally

The coverage value can be obtained while running the tests using
`pytest-cov` in the following way:

```bash
$ python -m pytest --cov={{ cookiecutter.project_slug }} tests/
```

A much more detailed guide on testing with `pytest` is available
[here](https://docs.pytest.org/en/8.0.x/how-to/index.html).
{%- endif %}
{%- endif %}

{% if cookiecutter.use_makim == "yes" -%}

## Automation Tasks with Makim

This project uses `makim` as  an automation tool. Please, check the
`.makim.yaml` file to check all the tasks available or run:

```bash
$ makim --help
```

{% elif cookiecutter.use_make == "yes" -%}

## Automation Tasks with Make

This project uses `make` as  an automation tool. Please, check the `Makefile`
to check all the tasks (targets) available.
{%- endif %}

## Release

This project uses semantic-release in order to cut a new release based on the
commit-message.

### Commit message format

**semantic-release** uses the commit messages to determine the consumer impact
of changes in the codebase. Following formalized conventions for commit
messages, **semantic-release** automatically determines the next
[semantic version](https://semver.org) number, generates a changelog and
publishes the release.

By default, **semantic-release** uses
[Angular Commit Message Conventions](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format).
The commit message format can be changed with the `preset` or `config` options\_
of the
[@semantic-release/commit-analyzer](https://github.com/semantic-release/commit-analyzer#options)
and
[@semantic-release/release-notes-generator](https://github.com/semantic-release/release-notes-generator#options)
plugins.

Tools such as [commitizen](https://github.com/commitizen/cz-cli) or
[commitlint](https://github.com/conventional-changelog/commitlint) can be used
to help contributors and enforce valid commit messages.

The table below shows which commit message gets you which release type when
`semantic-release` runs (using the default configuration):

| Commit message                                                 | Release type     |
| -------------------------------------------------------------- | ---------------- |
| `fix(pencil): stop graphite breaking when pressure is applied` | Fix Release      |
| `feat(pencil): add 'graphiteWidth' option`                     | Feature Release  |
| `perf(pencil): remove graphiteWidth option`                    | Chore            |
| `feat(pencil)!: The graphiteWidth option has been removed`     | Breaking Release |

Note: For a breaking change release, uses `!` at the end of the message prefix.

source:
<https://github.com/semantic-release/semantic-release/blob/master/README.md#commit-message-format>

As this project uses the `squash and merge` strategy, ensure to apply the commit
message format to the PR's title.
