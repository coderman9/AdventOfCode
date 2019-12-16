with open("input", "r") as f:
    ops = list(map(int, f.read().split(",")))

def run(ops, x, y):
    ops[1] = x
    ops[2] = y
    for i in range(0, len(ops), 4):
        if ops[i] == 99:
            return ops[0]
        try:
            if ops[i] == 1:
                ops[ops[i + 3]] = ops[ops[i + 1]] + ops[ops[i + 2]]
            elif ops[i] == 2:
                ops[ops[i + 3]] = ops[ops[i + 1]] * ops[ops[i + 2]]
        except:
            print(ops[i + 1], ops[i + 2], ops[i + 2], ops[i + 3])
            print("Skipping {}, {}".format(x, y))
            return None

for i in range(100):
    for j in range(100):
        if run(ops.copy(), i, j) == 19690720:
            print(100*i + j)
