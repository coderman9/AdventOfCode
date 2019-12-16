with open("input", "r") as f:
    input = f.readlines()

def f(x):
    q = x//3 - 2
    if q > 0:
        q += f(q)
    return max(q, 0)

r = sum([f(int(x)) for x in input])

print(r)
