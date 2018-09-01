import json

def load_annotation(filepath):
    with open(filepath) as file:
        annotations = json.load(file)
    return annotations