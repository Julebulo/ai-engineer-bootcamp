from toolkit.reader import read_file

def analyze_text(text):
    content = read_file(text)
    characters = len(content)
    words = len(content.split())
    lines = len(content.splitlines())
    result = {
        "characters": characters,
        "words": words,
        "lines": lines
    }
    return result