# graders

[![Release](https://img.shields.io/github/v/release/nlile/graders)](https://img.shields.io/github/v/release/nlile/graders)
[![Build status](https://img.shields.io/github/actions/workflow/status/nlile/graders/main.yml?branch=main)](https://github.com/nlile/graders/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/nlile/graders/branch/main/graph/badge.svg)](https://codecov.io/gh/nlile/graders)
[![Commit activity](https://img.shields.io/github/commit-activity/m/nlile/graders)](https://img.shields.io/github/commit-activity/m/nlile/graders)
[![License](https://img.shields.io/github/license/nlile/graders)](https://img.shields.io/github/license/nlile/graders)

This is a template repository for Python projects that use Poetry for their dependency management.

- **Github repository**: <https://github.com/nlile/graders/>
- **Documentation** <https://nlile.github.io/graders/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b master
git add .
git commit -m "init commit"
git remote add origin git@github.com:nlile/graders.git
git push -u origin master
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/nlile/graders/settings/secrets/actions/new).
- Create a [new release](https://github.com/nlile/graders/releases/new) on Github.
- Create a new tag in the form `*.*.*`.
- For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
