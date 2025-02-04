# APS API/CLI library

Set up virtual environment:

```
$ pipenv install -d
```

Enter the venv

```
$ pipenv shell
```

Run all unit tests

```
$ pytest
```

Run all unit tests with extra logging

```
$ pytest -v
```

Run all unit tests and capture covarage

```
$ coverage run -m pytest
```

Display coverage report

```
$ coverage report
```

Install CLI in you virtual environment

```
$ pip install -e .
```

Run commands eg:

```
$ vmx-aps --api-key-file ~/Downloads/api-key.json get_version
```
