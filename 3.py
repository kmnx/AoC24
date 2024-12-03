with open("3.txt", "r") as myfile:
    data = myfile.readlines()

# part 1
total = 0

for line in data:
    res = 0
    muls = line.split("mul(")
    for candidate in muls:
        if candidate[0].isnumeric():
            next_split = candidate.split(")")
            hopeful_split = next_split[0].split(",")
            if len(hopeful_split) == 2:
                if hopeful_split[0].isnumeric() and hopeful_split[1].isnumeric():
                    res += int(hopeful_split[0]) * int(hopeful_split[1])
    total += res

print(total)


# part 2
res = 0
longstr = ""
# create one huge string if it isn't one already
for line in data:
    longstr += line

# split into blocks that will definitely start with "do()"
do_blocks = longstr.split("do()")

# within those blocks, cut off everything after the first "don't()"
trimmed_do_blocks = []
for block in do_blocks:
    split_blocks = block.split("don't()")
    trimmed_do_blocks.append(split_blocks[0])

# whatever remains has "do()"-status, collect the mul()-candidates
candidates = []
for candidate in trimmed_do_blocks:
    mul_candidates = candidate.split("mul(")
    for candidate in mul_candidates:
        candidates.append(candidate)

# check if the candidates are valid and calculate the result
for candidate in candidates:
    if candidate == "":
        continue
    if candidate[0].isnumeric():
        next_split = candidate.split(")")
        hopeful_split = next_split[0].split(",")
        if len(hopeful_split) == 2:
            if hopeful_split[0].isnumeric() and hopeful_split[1].isnumeric():
                res += int(hopeful_split[0]) * int(hopeful_split[1])

print(res)
