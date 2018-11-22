import random

def valid (set):
    if set[0][0]==set[-1][0]:
        return False
    for i in range(len(set)-1):
        if set[i][0]==set[i+1][0]:
            return False
    return True

group1 = "group1.txt"
group2 = "group2.txt"

with open(group1,'r') as fo:
    users1 = [(i,a.strip().split(',')[0],a.strip().split(',')[1]) for i,a in enumerate(fo.readlines())]
with open(group2,'r') as fo:
    users2 = [(i,a.strip().split(',')[0],a.strip().split(',')[1]) for i,a in enumerate(fo.readlines())]

users = users1 + users2

random.shuffle(users)
while not valid(users):
    print("SKIPPING")
    print(users)
    random.shuffle(users)
print(users)
