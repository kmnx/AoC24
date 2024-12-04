with open("4.txt", "r") as myfile:
    data = myfile.readlines()


xmas_array = []
for line in data:
    xmas_array.append(line.strip())

xmas_counter = 0
for h, line in enumerate(xmas_array):
    for v, char in enumerate(line):
        if char == "X":
            if h > 2:
                if (
                    xmas_array[h - 1][v] == "M"
                    and xmas_array[h - 2][v] == "A"
                    and xmas_array[h - 3][v] == "S"
                ):
                    xmas_counter += 1
            if h > 2 and v < len(line) - 3:
                if (
                    xmas_array[h - 1][v + 1] == "M"
                    and xmas_array[h - 2][v + 2] == "A"
                    and xmas_array[h - 3][v + 3] == "S"
                ):
                    xmas_counter += 1
            if v < len(line) - 3:
                if (
                    xmas_array[h][v + 1] == "M"
                    and xmas_array[h][v + 2] == "A"
                    and xmas_array[h][v + 3] == "S"
                ):
                    xmas_counter += 1
            if h < len(xmas_array) - 3 and v < len(line) - 3:
                if (
                    xmas_array[h + 1][v + 1] == "M"
                    and xmas_array[h + 2][v + 2] == "A"
                    and xmas_array[h + 3][v + 3] == "S"
                ):
                    xmas_counter += 1
            if h < len(xmas_array) - 3:
                if (
                    xmas_array[h + 1][v] == "M"
                    and xmas_array[h + 2][v] == "A"
                    and xmas_array[h + 3][v] == "S"
                ):
                    xmas_counter += 1
            if h < len(xmas_array) - 3 and v > 2:
                if (
                    xmas_array[h + 1][v - 1] == "M"
                    and xmas_array[h + 2][v - 2] == "A"
                    and xmas_array[h + 3][v - 3] == "S"
                ):
                    xmas_counter += 1
            if v > 2:
                if (
                    xmas_array[h][v - 1] == "M"
                    and xmas_array[h][v - 2] == "A"
                    and xmas_array[h][v - 3] == "S"
                ):
                    xmas_counter += 1
            if h > 2 and v > 2:
                if (
                    xmas_array[h - 1][v - 1] == "M"
                    and xmas_array[h - 2][v - 2] == "A"
                    and xmas_array[h - 3][v - 3] == "S"
                ):
                    xmas_counter += 1


print("xmas-count:", xmas_counter)

xmas_counter = 0
for h, line in enumerate(xmas_array):
    for v, char in enumerate(line):
        if char == "A":
            charpool = []
            if (
                (h > 0)
                and (h < len(xmas_array) - 1)
                and (v > 0)
                and (v < len(line) - 1)
            ):
                charpool.append(xmas_array[h + 1][v + 1])
                charpool.append(xmas_array[h + 1][v - 1])
                charpool.append(xmas_array[h - 1][v + 1])
                charpool.append(xmas_array[h - 1][v - 1])
                if charpool.count("M") == 2 and charpool.count("S") == 2:
                    if not (xmas_array[h + 1][v + 1] == xmas_array[h - 1][v - 1]):
                        xmas_counter += 1

print("mas-count: ", xmas_counter)
