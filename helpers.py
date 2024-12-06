def open_file(path):
    with open(path, "r") as file:
        data = [line for line in file]
        return data