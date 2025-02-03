import os
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"
from embedchain import App

DATA_DIR = "./data"
ALLOW_LIST = [".pdf"]

app = App.from_config(config_path="config.yaml")

data_sources = app.get_data_sources()
for d in os.listdir(DATA_DIR):
    for ext in ALLOW_LIST:
        filename = os.path.join(DATA_DIR, d)
        for item in data_sources:
            if item["data_value"] == filename:
                continue

        if d.endswith(ext):
            if ext == ".pdf":
                app.add(filename, data_type='pdf_file')
            else:
                app.add(filename)

print("==== DATA SOURCES ====")
data_sources = app.get_data_sources()
for d in data_sources:
    print(d)
print("======================")

# TODO: Edit question here
result = app.query("Who are you?")

print("==== OUTPUT ====")
print(result)
print("================")
