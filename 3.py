with open("3.txt", "r") as myfile:
    data = myfile.readlines()

# part 1
total = 0

for line in data:
    res = 0
    muls = line.split("mul(")
    for item in muls:
        if item[0].isnumeric():
            next_split = item.split(")")
            hopeful = next_split[0].split(",")
            if len(hopeful) == 2:
                if hopeful[0].isnumeric() and hopeful[1].isnumeric():
                    res += int(hopeful[0]) * int(hopeful[1])
    total += res

print(total)


# part 2
res = 0
longstr = ""
# create one huge string if it isn't one already
for line in data:
    longstr += line

# split into blocks that will definitely start with "do()"
dosplit = longstr.split("do()")

# within those blocks, cut off everything after the first "don't()"
realdos = []
for block in dosplit:
    dontsplits = block.split("don't()")
    realdos.append(dontsplits[0])

# whatever remains has "do()"-status, collect the mul()-candidates
candidates = []
for item in realdos:
    multcand = item.split("mul(")
    for cand in multcand:
        candidates.append(cand)

# check if the candidates are valid and calculate the result
for item in candidates:
    if item == "":
        continue
    if item[0].isnumeric():
        next_split = item.split(")")
        hopeful = next_split[0].split(",")
        if len(hopeful) == 2:
            if hopeful[0].isnumeric() and hopeful[1].isnumeric():
                res += int(hopeful[0]) * int(hopeful[1])

print(res)
