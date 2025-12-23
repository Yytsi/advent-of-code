from aocd import data
from functools import cache

g = data.split("\n")
n = len(g)
g = [list("." * (n+4)),
     *[f"x{row}x" for row in g],
     list(";" * (n+4))]

@cache
def f(y, x): return 1 if y == n else f(y+1, x-1) + f(y+1, x+1) if g[y+1][x] == "^" else f(y+1, x)
print(f(2, g[1].index("S")))



# m = {}
# def f(y, x): return 1 if y == n else m[y,x] if (y,x) in m else m.setdefault((y,x), (g[y+1][x] == "^" and (f(y+1, x-1) + f(y+1, x+1))) or f(y+1, x))