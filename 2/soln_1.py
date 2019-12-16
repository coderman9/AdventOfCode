with open("input", "r") as f:
    ops = list(map(int, f.read().split(",")))

for i in range(0, len(ops), 4):
    if ops[i] == 99:
        print(ops)
        exit
    if ops[i] == 1:
        ops[ops[i + 3]] = ops[ops[i + 1]] + ops[ops[i + 2]]
    elif ops[i] == 2:
        ops[ops[i + 3]] = ops[ops[i + 1]] * ops[ops[i + 2]] 
