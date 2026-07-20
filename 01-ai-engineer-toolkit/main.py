import sys

from toolkit.reader import read_file
from toolkit.analyzer import analyze_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    stats = analyze_text(text)
    print(stats)