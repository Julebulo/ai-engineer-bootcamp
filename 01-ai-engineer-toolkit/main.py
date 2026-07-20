import sys

from toolkit.reader import read_file
from toolkit.analyzer import stats_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    #data = read_file(file_path)
    # print(data)
    stats = stats_file(file_path)
    print(stats)