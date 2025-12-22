from aocd import data

g, t = [], 0
for r in data.split("\n"):
    if "-" in r:
        a, b = map(int, r.split("-"))
        g.append((a, -1))
        g.append((b, 1))
    elif r.isdigit(): g.append((int(r), 0))

print(sum((t:=t+v)<0 and v==0 for (x,v) in sorted(g)))