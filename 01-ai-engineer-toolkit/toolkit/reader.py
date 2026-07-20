def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def stats_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        characters = len(content)
        words = len(content.split())
        lines = len(content.splitlines())
        result = {
            "characters": characters,
            "words": words,
            "lines": lines
        }
    return result