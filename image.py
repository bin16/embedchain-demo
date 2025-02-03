import ollama

client = ollama.Client(
  host='http://localhost:11434',
)

# ollama pull llama3.2-vision
# https://ollama.com/library/llama3.2-vision
# TODO: edit content and your image filenames.
response = client.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': ['256x256.png'],
    }]
)

print(response)
