# coding-style

## Linting
- flake8: a multi-linter - it is a wrapper around the PyFlakes, pycodestyle, and Ned Batchelder's McCabe scripts and does a little more
  - NOTE: this is installed as a pre-commit hook and generally should not require manual running
    - more info: https://flake8.pycqa.org/en/latest/user/using-hooks.html
  ----
  - connect to container
  - install flake8: `pip install flake8`
  - run flake8: `flake8 /opt/app`
    - NOTE: see the `.flake8` config file for ignored items and config of flake8
  ----
  - to ignore a line add the `# noqa ###` tag

## Security
- bandit: a tool designed to find common security issues in Python code
  - NOTE: this is installed as a pre-commit hook and generally should not require manual running
    - more info: https://github.com/PyCQA/bandit#version-control-integration
  ----
  - connect to container
  - install bandit: `pip install bandit`
  - run bandit: `bandit -r /opt/app`
  ----
  - to ignore a line add the `#nosec` tag

## Style
- black: The Uncompromising Code Formatter
  - NOTE: this is installed as a pre-commit hook and generally should not require manual running
    - more info: https://pypi.org/project/black/#version-control-integration
  ----
  - install pre-commit: `pip install pre-commit`
  - use pre-commit to install the black pre-commit config: `pre-commit install`
  - more information can be found at [black](https://github.com/ambv/black)
