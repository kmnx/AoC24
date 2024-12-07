import helpers
data = helpers.open_file("6.txt")

print(data)

directions = {"v":[1,0],"^":[-1,0],"<":[0,-1],">":[0,1]}






turns = []

def walk(pos,direction,room):
    while True:
        try:
            if room[pos[0] + direction[0]][pos[1] + direction[1]] != "#":
                room[pos[0]][pos[1]] = "X"
                pos = pos[0] + direction[0],pos[1] + direction[1]
            else:
                turns.append(pos)
                if direction[0] == -1:
                    direction = (0,1)
                elif direction[0] == 1:
                    direction = (0,-1)
                elif direction[1] == -1:
                    direction = (-1,0)
                elif direction[1] == 1:
                    direction = (1,0)
            #for line in room:
            #    print(line)
            #print(" ")
        except IndexError:
            room[pos[0]][pos[1]] = "X"
            break


def get_position(room):
    direction = None
    pos = [0,0]
    for i,line in enumerate(room):
        for k,char in enumerate(line):
            if char in directions:
                pos = (i,k)
                direction = directions[char]
                print(pos,direction)
                #input()
    return pos,direction





def main():
    room = []
    for line in data:
        room_line = [c for c in line]
        room.append(room_line)

    for line in room:
        print(line)
    pos, direction = get_position(room)
    walk(pos,direction,room)


    count = 0
    for line in room:
        for c in line:
            if c == "X":
                count += 1
        print(line)
    print(count)

    print(turns)



if __name__ == "__main__":
    main()
