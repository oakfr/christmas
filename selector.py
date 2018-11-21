
group1 = "group1.txt"
group2 = "group2.txt"

with open(group1,'r') as fo:
    users1 = [(i,a.strip().split(',')[0],a.strip().split(',')[1]) for i,a in enumerate(fo.readlines())]
with open(group2,'r') as fo:
    users2 = [(i,a.strip().split(',')[0],a.strip().split(',')[1]) for i,a in enumerate(fo.readlines())]
print(users1)

