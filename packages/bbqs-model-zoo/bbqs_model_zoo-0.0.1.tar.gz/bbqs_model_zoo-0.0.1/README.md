# The Sensein's python package template repo

Welcome to the [Sensein](https://sensein.group/) python template repo! 
This template is here to help you kick off your projects with a clean and efficient setup. 
It's inspired by the [python template by the Child Mind Institute](https://github.com/childmindresearch/template-python-repository) (thanks you!). Our version diverges in its setup process and in both the variety and quantity of automated features included.

Just follow these steps, and you'll be on your way:
1. **Choose a unique package name:** First off, you need a cool name for your package. To make sure it's not already taken on PyPI, head over to `https://pypi.org/project/bbqs-model-zoo/`. If you get a "Not Found" page, you're likely good to go!

2. **Use this template:** Go to the GitHub page for this template. You'll find a "Use this template" button on the top right. Click it to start setting up your project with the template's structure.

3. **Configure your project:** During the setup, you'll specify some basics like your project's name and whether it's public or private. You will be able to change this info in the future, no pressure!

4. **Add GitHub Secrets:** For automated processes, add these secrets to your GitHub repo:

- `PYPI_TOKEN`: Your token for PyPI, allowing GitHub Actions to publish your package.
- `AUTO_ORG_TOKEN`: A token for automated organization actions (this is useful for using [auto](https://github.com/intuit/auto) for automatic changelog generation).
- `CODECOV_TOKEN`: Your [Codecov](https://about.codecov.io/) token for reporting code coverage.

To obtain these tokens:
- For `PYPI_TOKEN`, log in to your PyPI account, go to your account settings, and create an API token. Alternatively, ask the admin of your organization to do so.
- `AUTO_ORG_TOKEN` is a personal access token from GitHub, used for actions requiring organization-level permissions. Generate one in your GitHub settings under Developer settings > Personal access tokens. Alternatively, if the repo is under your organization GitHub, please, ask the admin of your organization to provide one.
- For `CODECOV_TOKEN`, sign up or log in to Codecov, add your repository, and you'll be provided with a token.

To add these tokens:
Go to your repository on GitHub, click on "Settings" > "Secrets" > "Actions", then click on "New repository secret". Name your secret (e.g., `PYPI_TOKEN`) and paste the token value. Repeat this for each token.

5. **Clone the repo:** Once your repository is set up, clone it to your local machine.

6. **Replace placeholders with custom values**: Please, run `python template_setup.py --package-name bbqs-model-zoo --package-repo-without-git-extension https://github.com/brain-bbqs/bbqs-model-zoo --github-nickname hvgazula --codecov-token 5ca98d8e-8fb2-4e50-8879-f86cf22a121a --email hvgazula@umich.edu`. 
For example, `python template_setup.py --package-name pipepal --package-repo-without-git-extension https://github.com/fabiocat93/pipepal --github-nickname fabiocat93 --codecov-token IQR1RCYMAA --email fabiocat@mit.edu`. This will replace some placeholders in the entire directory (including folder names, file names, file content) with your custom info:
- bbqs-model-zoo (e.g., `pipepal`)
- https://github.com/brain-bbqs/bbqs-model-zoo (e.g., `https://github.com/sensein/pipepal`)
- hvgazula (e.g., `sensein`)
- 5ca98d8e-8fb2-4e50-8879-f86cf22a121a (e.g.,`ABC0DEFGHI`)
- hvgazula@umich.edu (e.g., `sensein@mit.edu`)
It will also enable GitHub custom automation and delete the `template_setup.py` (you won't need that anymore).

7. **Adjust `pyproject.toml`:** Please, double-check `pyproject.toml` and update it with some custom info, if needed (i.e., `description`, `authors`, `maintainers`, `description`, `homepage`, `repository`, `keywords`, and `classifiers`). No need to touch `version`. This will be automatically handled by the package.

8. **Update README.md:** Replace the content of this README.md with information specific to your project.

9. **Install poetry:** Poetry is a fantastic tool for managing dependencies and packaging. If you haven't installed it yet, check out their [documentation](https://python-poetry.org/docs/) for guidance. It's pretty straightforward.

10. **Verify poetry setup:** Run `poetry --help` to ensure everything is set up correctly. To verify that the project folder is all in order, you can run `poetry check`.

11. **Install dependencies:** Get all your project's dependencies in place by running `poetry install --with dev`.

12. **Secure your package name:** Even if you're not quite ready to publish, consider securing your package name on PyPI. You can do this by publishing a dummy version (0.0.1) of your package with `poetry publish --build`.

13. **Commit and push:** Now's the time to add (e.g., `git add .`) and commit (e.g., `git commit -m "here goes a wonderful message"`) your changes. Consider adding a tag for your initial version (recommended), like `git tag 0.0.1`, then push it all to GitHub with `git push --tags` and `git push origin main`.

14. **Check GitHub actions:** If your push was successful, it'll trigger some GitHub Actions like code quality checks and tests. Make sure everything passes!

15. **Work in dev branch:** For future changes, create a `dev` branch and make your updates there. Use pull requests to merge these changes into the main branch.

16. **Releasing new versions:** If you want to release a new version of your package, add a "release" label to your pull request. This will trigger all the necessary actions to update the version tag, create a changelog, release the new version, and even create/update your package documentation.

17. **Set up API documentation:** After your first successful pull request, set up your API documentation website. Go to your repository's settings, find the GitHub Pages section, and select `docs` as the source. You'll get a link to your API docs.

18. **[Bonus] Customize issue and pull request remplates:** Optionally, you can customize your issue and pull request remplates from the `.github` folder.

That's it! With these steps, you're well on your way to creating an awesome Python package. Keep up the great work, and **happy coding**!


# The ```bbqs-model-zoo``` repo

[![Build](https://github.com/brain-bbqs/bbqs-model-zoo/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/brain-bbqs/bbqs-model-zoo/actions/workflows/test.yaml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/hvgazula/bbqs-model-zoo/branch/main/graph/badge.svg?token=5ca98d8e-8fb2-4e50-8879-f86cf22a121a)](https://codecov.io/gh/hvgazula/bbqs-model-zoo)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![PyPI](https://img.shields.io/pypi/v/bbqs-model-zoo.svg)](https://pypi.org/project/bbqs-model-zoo/)
[![Python Version](https://img.shields.io/pypi/pyversions/bbqs-model-zoo)](https://pypi.org/project/bbqs-model-zoo)
[![License](https://img.shields.io/pypi/l/bbqs-model-zoo)](https://opensource.org/licenses/Apache-2.0)

[![pages](https://img.shields.io/badge/api-docs-blue)](https://hvgazula.github.io/bbqs-model-zoo)

Welcome to the ```bbqs-model-zoo``` repo! This is a Python package for doing incredible stuff.

**Caution:**: this package is still under development and may change rapidly over the next few weeks.

## Features
- A few
- Cool
- Things
- These may include a wonderful CLI interface.

## Installation
Install this package via :

```sh
pip install bbqs-model-zoo
```

Or get the newest development version via:

```sh
pip install git+https://github.com/brain-bbqs/bbqs-model-zoo.git
```

## Quick start
```Python
from bbqs-model-zoo.app import hello_world

hello_world()
```

## To do:
- [ ] A
- [ ] lot
