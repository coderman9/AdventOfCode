with open("input", "r") as f:
    input = f.readlines()

def f(x):
    return x//3 - 2

print(sum([f(int(c)) for c in input]))
