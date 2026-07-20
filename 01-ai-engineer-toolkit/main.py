import sys

<<<<<<< HEAD
from toolkit.reader import read_file
from toolkit.analyzer import stats_file
=======
from toolkit.reader import read_file, stats_file
>>>>>>> 726b9b90eb1b45f25775df0e9b449d7f1d271ae7

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    #data = read_file(file_path)
    # print(data)
    stats = stats_file(file_path)
    print(stats)