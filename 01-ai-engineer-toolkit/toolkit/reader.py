def reader(file_path):
    with open(file_path, 'r') as file:
        read_data = file.read()
    return read_data