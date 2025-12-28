from aocd import data

g = [list(map(int, row.split(","))) for row in data.split("\n")]

n = len(g)
p = list(range(n))

top = lambda x: x if p[x] == x else top(p[x])

distances_and_points = []

for i in range(n):
    for j in range(i+1, n):
        x1, y1, z1 = g[i]
        x2, y2, z2 = g[j]
        cur_d = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
        distances_and_points.append((cur_d, i, j))

for (dist, i, j) in sorted(distances_and_points)[:1000]:
    p[top(i)] = top(j)

root_heads_instances = list(map(top, p))

m = sorted(root_heads_instances.count(e) for e in set(p))
print(m[-1] * m[-2] * m[-3])