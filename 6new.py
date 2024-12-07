import copy

with open("6.txt", "r") as myfile:
    data = myfile.readlines()
def print_room(room):
    for line in room:
        room_line = ""
        for char in line:
            room_line += char
        
        print(room_line)

walked_path = []
def walk(pos,direction,room):
    exited = False
    room[pos[0]][pos[1]] = "X"
    
    while not exited:
        if pos[0] + direction[0] < 0 or \
            pos[1] + direction[1] < 0 or \
            pos[0] + direction[0] == len(room) or \
            pos[1] + direction[1] == len(room):
                exited = True
                print_room(room)
                return room

        elif room[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            while room[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
                if direction[0] == -1:
                    direction = (0,1)
                elif direction[0] == 1:
                    direction = (0,-1)
                elif direction[1] == -1:
                    direction = (-1,0)
                elif direction[1] == 1:
                    direction = (1,0)

        
        pos = pos[0] + direction[0],pos[1] + direction[1]
        room[pos[0]][pos[1]] = "X"
        walked_path.append(pos)
    
        


def find_guard_pos(room):
    for line in room:
        for char in line:
            if char in ["^", "v", "<", ">"]:
                guard_pos = (room.index(line), line.index(char))
                return guard_pos
            
def it_loops(pos,direction,room):
    exited = False
    looping = False
    visited = []
    while not (exited or looping):
        room[pos[0]][pos[1]] = "X"
        #print_room(room)
        #print("    ")
        
        if pos[0] + direction[0] < 0 or \
            pos[1] + direction[1] < 0 or \
            pos[0] + direction[0] == len(room) or \
            pos[1] + direction[1] == len(room):
                exited = True

        elif room[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            if pos in visited:
                looping = True
            else:
                while room[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
                    if direction[0] == -1:
                        direction = (0,1)
                    elif direction[0] == 1:
                        direction = (0,-1)
                    elif direction[1] == -1:
                        direction = (-1,0)
                    elif direction[1] == 1:
                        direction = (1,0)
                visited.append(pos)
            
        else:
            pos = pos[0] + direction[0],pos[1] + direction[1]
            
            
                
    if looping:
        return True
    elif exited:
        return False

def find_loops(pos,direction,room):
    original_room = copy.deepcopy(room)
    exited = False
    loopcount = 0
    while not exited:
        room[pos[0]][pos[1]] = "X"

        if pos[0] + direction[0] < 0 or \
            pos[1] + direction[1] < 0 or \
            pos[0] + direction[0] == len(room) or \
            pos[1] + direction[1] == len(room):
                exited = True

        elif room[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            if direction[0] == -1:
                direction = (0,1)
            elif direction[0] == 1:
                direction = (0,-1)
            elif direction[1] == -1:
                direction = (-1,0)
            elif direction[1] == 1:
                direction = (1,0)

        else:
            new_room = copy.deepcopy(original_room)
            new_room[pos[0]+direction[0]][pos[1]+direction[1]] = "#"
            #print_room(new_room)
            if it_loops(pos,direction,new_room):
                loopcount += 1
                #print(loopcount)
            pos = pos[0] + direction[0],pos[1] + direction[1]
            
            
    return loopcount
def a_new_hope(walked_path,room):
    loopcount = 0
    for pos in range(len(walked_path)-1):
        looptestroom = copy.deepcopy(room)
        direction = (walked_path[pos+1][0] - walked_path[pos][0],walked_path[pos+1][1] - walked_path[pos][1])
        position = walked_path[pos]
        block_position = position[0] + direction[0],position[1] + direction[1]
        looptestroom[position[0] + direction[0]][position[1] + direction[1]] = "#"
        print(position,direction)
        if it_loops(position,direction,looptestroom):
            loopcount += 1
            print(loopcount)
        
    print(loopcount)

def main():
    original_room = []
    for line in data:
        room_line = [c for c in line.strip()]
        original_room.append(room_line)

    for line in original_room:
        print(line)

    guard_pos = find_guard_pos(original_room)
    print(guard_pos)
    room = copy.deepcopy(original_room)
    
    walked = walk(pos=guard_pos,direction=(-1,0),room=room)
    visited_count = 0
    for line in walked:
        for char in line:
            if char == "X":
                visited_count += 1
    print(visited_count)
    new_room = copy.deepcopy(original_room)
    print(guard_pos)
    #loops = find_loops(pos=guard_pos,direction=(-1,0),room=new_room)
    #print(loops)
    print(walked_path)
    print(a_new_hope(walked_path,original_room))
                

if __name__ == "__main__":
    main()