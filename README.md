## Python Environment

Python 3.12 is recommended. For Python 3.13, some packages have no binary files, and hard to build.

### Virtualenv (Optional but very helpful)

```sh
pip install virtualenv

virtualenv --py /path/to/python/3.12 ./venv

# activate virtual environment

# macOS or Linux
source ./venv/bin/activate

# Windows
./venv/Scripts/activate.bat # or .ps1
```

## Install Packages

```sh
pip install embedchain ollama
```

## Pull Models

```sh
ollama pull deepseek-r1
ollama pull nomic-embed-text
```
