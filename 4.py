with open("4.txt", "r") as myfile:
    data = myfile.readlines()

xmas_array = [line for line in data]
xmas_counter = 0
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


# part 1
def check_xmas(h, v, dh, dv):
    pattern = "MAS"
    return all(
        0 <= h + (i + 1) * dh < len(xmas_array)
        and 0 <= v + (i + 1) * dv < len(line)
        and xmas_array[h + (i + 1) * dh][v + (i + 1) * dv] == pattern[i]
        for i in range(len(pattern))
    )


for h, line in enumerate(xmas_array):
    for v, char in enumerate(line):
        if char == "X":
            for dh, dv in directions:
                if check_xmas(h, v, dh, dv):
                    xmas_counter += 1

print("xmas-count: ", xmas_counter)

# part 2
xmas_counter = 0
for h, line in enumerate(xmas_array):
    for v, char in enumerate(line):
        if char == "A":
            if (
                (0 < h < len(xmas_array) - 1)
                and (0 < v < len(line) - 1)
                and not (xmas_array[h + 1][v + 1] == xmas_array[h - 1][v - 1])
            ):
                charpool = [
                    xmas_array[h + 1][v + 1],
                    xmas_array[h + 1][v - 1],
                    xmas_array[h - 1][v + 1],
                    xmas_array[h - 1][v - 1],
                ]

                if charpool.count("M") == 2 and charpool.count("S") == 2:
                    xmas_counter += 1

print("mas-count: ", xmas_counter)
