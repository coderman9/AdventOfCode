with open("input", "r") as f:
    input = f.readlines()

pos1 = [(0,0)]
pos2 = [(0,0)]
for e, inp in enumerate(input):
    for r in inp.split(","):
        if r[0] == "U":
            x, y = 0, 1
        if r[0] == "D":
            x, y = 0, -1
        if r[0] == "R":
            x, y = 1, 0
        if r[0] == "L":
            x, y = -1, 0
        for i in range(int(r[1:])):
            if e:
                pos2.append((pos1[-1][0] + x, pos1[-1][1] + y))
            else:
                pos1.append((pos1[-1][0] + x, pos1[-1][1] + y))

pos1 = sorted(pos1, key = lambda x: abs(x[0]) + abs(x[1]))

print(pos2[:100])

for p in pos1[1:]:
    if p in pos2:
        print(p)
        exit()
