# gradable

[![Release](https://img.shields.io/github/v/release/nlile/gradable)](https://img.shields.io/github/v/release/nlile/gradable)
[![Build status](https://img.shields.io/github/actions/workflow/status/nlile/gradable/master.yml?branch=master)](https://github.com/nlile/gradable/actions/workflows/master.yml?query=branch%3Amaster)
[![codecov](https://codecov.io/gh/nlile/gradable/branch/master/graph/badge.svg)](https://codecov.io/gh/nlile/gradable)
[![Commit activity](https://img.shields.io/github/commit-activity/m/nlile/gradable)](https://img.shields.io/github/commit-activity/m/nlile/gradable)
[![License](https://img.shields.io/github/license/nlile/gradable)](https://img.shields.io/github/license/nlile/gradable)

Gradable reward signals

- **Github repository**: <https://github.com/nlile/gradable/>
- **Documentation** <https://nlile.github.io/gradable/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b master
git add .
git commit -m "init commit"
git remote add origin git@github.com:nlile/gradable.git
git push -u origin master
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to master, or when you create a new release.

To finalize the set-up for publishing to PyPI or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/nlile/gradable/settings/secrets/actions/new).
- Create a [new release](https://github.com/nlile/gradable/releases/new) on Github.
- Create a new tag in the form `*.*.*`.
- For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
