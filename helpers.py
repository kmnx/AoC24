def open_file(path):
    with open(path, "r") as file:
        data = [line.strip() for line in file]
        return data