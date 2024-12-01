with open ("1.txt", "r") as myfile:
    data = myfile.readlines()

list_one = []
list_two = []
for line in data:
    list_one.append(line.split()[0])
    list_two.append(line.split()[1])

list_one = sorted(list_one)
list_two = sorted(list_two)

tempdist = 0
for k,m in zip(list_one, list_two):
    tempdist += abs(int(k)-int(m))

print(tempdist)

tempdist = 0
for number in list_one:
    appearancecount = 0
    for number2 in list_two:
        if number == number2:
            appearancecount += 1
    tempdist += appearancecount * int(number)
print(tempdist)