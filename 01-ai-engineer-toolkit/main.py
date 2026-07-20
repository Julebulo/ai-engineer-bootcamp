import sys
import toolkit.reader

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    data = toolkit.reader.reader(file_path)
    print(data)