def analyze_text(text):
    characters = len(text)
    words = len(text.split())
    lines = len(text.splitlines())
    result = {
        "characters": characters,
        "words": words,
        "lines": lines
    }
    return result