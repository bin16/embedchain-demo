## main.py

auto load pdf files in data/ dir, and answer the given question.

```sh
# ollama pull llama3.2
# ollama pull nomic-embed-text
python main.py
```

## image.py

send image to llama3.2-vision and answer question

```sh
# ollama pull llama3.2-vision
python image.py
```

----

## Python Environment

**Python 3.12** is recommended. For Python 3.13, some packages have no binary files, and hard to build.

### Install Virtualenv (Optional but very helpful)

```sh
pip install virtualenv

virtualenv --py /path/to/python/3.12 ./venv
```

Activate virtual environment

```sh
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
ollama pull llama3.2
ollama pull nomic-embed-text
```

### LLM

#### llama3.2

https://ollama.com/library/llama3.2

#### llama3.2-vision

https://ollama.com/library/llama3.2-vision

### Embedding models

https://ollama.com/blog/embedding-models

#### nomic-embed-text

https://ollama.com/library/nomic-embed-text
