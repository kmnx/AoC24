# sent from my iPhon

with open("5.txt", "r") as myfile:
    data = myfile.readlines()


rules = [line.strip() for line in data if "|" in line]
orderlists = [line.strip() for line in data if "|" not in line and line.strip() != ""]

gt_dict = {}
lt_dict = {}

total = 0
wrong = []
for ordering in orderlists:
    l = ordering.strip().split(",")
    correct = True
    #print("testing a new ordering")
    #print(l)
    for i,pg in enumerate(l):
        if correct == False:
            break
        for rule in rules:
            if correct == False:
                break
            bef,aft = rule.strip().split("|")[0],rule.split("|")[1]
            if (bef == pg):
                if bef in l and aft in l:
                    if l.index(bef) < l.index(aft):
                        pass
                    else:
                        #print("both in but wrong")
                        correct = False
                        wrong.append(l)
                        break
                else:
                    pass
        if correct and i == len(l)-1:
            #print("correct",l,l[int((len(l)-1)/2)])
            total += int(l[int((len(l)-1)/2)])
print(total)
fixed_list = []

def fix(l, k=0, fixed=False):
    #for i,num in enumerate(l):
    for i in range(k,len(l)):
        num = l[i]
        #print("currently at", l, i, fixed)
        if fixed and i == len(l)-1:
            #print("fixed and len",l)
            return l,True
        else:
            for rule in rules:
                bef,aft = rule.strip().split("|")[0],rule.split("|")[1]
                if (bef == num):
                    if bef in l and aft in l:
                        #print("testing",l,bef,aft)
                        if l.index(bef) < l.index(aft):
                            pass
                        else:
                            #print("both in but wrong")
                            l[l.index(bef)],l[l.index(aft)] = l[l.index(aft)],l[l.index(bef)]
                            #print("swapped",l)
                            newline, fixed = fix(l, i, False)
                            #print("returning",newline)
                            return newline, fixed
                    else:
                        pass
            if i == len(l)-1:
                #print("fixed at end",l)
                return l,True

for line in wrong:
    newline, fixed = fix(line, 0, False)
    fixed_list.append(newline)

#print(fixed_list)
newtotal=0
for l in fixed_list:
    newtotal += int(l[int((len(l)-1)/2)])
print("fixed",newtotal)
