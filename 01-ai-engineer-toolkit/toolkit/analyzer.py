from toolkit.reader import read_file

def stats_file(file_path):
    content = read_file(file_path)
    characters = len(content)
    words = len(content.split())
    lines = len(content.splitlines())
    result = {
        "characters": characters,
        "words": words,
        "lines": lines
    }
    return result