# EZPY Logs

Package for my personal use, swiss knife logging :
- When logging, has a nice formatter with file line and datetime
- Colorful logger
- Easy import / use
- Save to files, with errors
- Auto delete old logs

## Install

```
```

## Usage

```sh
uv run python hello.py
```

## Dev

### Local env setup

```sh
uv venv
venv/bin/avtivate
uv sync
```

### TESTING 

```sh
uv run python -m pytest -s -v tests/test_logger.py
```

### Publishing

Change version in `pyproject.toml`

```sh
rm -rf dist
python -m build
twine upload dist/*
```