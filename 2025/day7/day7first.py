from aocd import data

g = data.splitlines()
n = len(g)
g = [list("." * (n+4)), *[list("x" + row + "x") for row in g], list(";" * (n+4))]
g[2][g[1].index("S")] = "|"

c = 0

for y in range(1,n+1):
    for x in range(1,n+1):
        if g[y][x] != "^" and g[y-1][x] == "|":
            g[y][x] = "|"
        if g[y][x] + g[y+1][x] == "|^":
            g[y+1][x-1] = "|"
            g[y+1][x+1] = "|"
            c += 1

print(c)