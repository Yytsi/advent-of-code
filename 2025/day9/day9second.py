from aocd import data
from itertools import *
from collections import deque

g = [list(map(int, row.split(","))) for row in data.split("\n")]
n = len(g)
og = [[0,0] for i in range(n)] # Store the original coordinates

uniqs = []
for i in range(2):
    for v in g:
        uniqs.append(v[i])


# Index compress all coordinates that are accessed
for (a, b) in [*zip(g, g[1:]), (g[-1], g[0])]:
    x1, y1 = a
    x2, y2 = b
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    max_x = max(x1, x2)
    max_y = max(y1, y2)
    uniqs.append(min_x)
    uniqs.append(min_y)
    uniqs.append(max_x)
    uniqs.append(max_y)
    uniqs.append(min_x-1)
    uniqs.append(min_y-1)


uniqs = list(sorted(set(uniqs)))

for i in range(2):
    for j in range(n):
        og[j][i] = g[j][i]
        g[j][i] = uniqs.index(g[j][i]) + 1


M = 500*5
grid = [[0] * M for j in range(M)]

# Fill the 'edges' of the shape (useful for BFS)
for (a, b) in [*zip(g, g[1:]), (g[-1], g[0])]:
    x1, y1 = a
    x2, y2 = b
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    grid[y1][x1] = 1
    while x1 < x2:
        x1 += 1
        grid[y1][x1] = 1
    while y1 < y2:
        y1 += 1
        grid[y1][x1] = 1


# Fill everything around the main shape with -INF so we can detect if a rectangle touches any 'illegal' space
bfs_queue = deque()
bfs_queue.append([0, 0])
visited = []

while len(bfs_queue):
    t = bfs_queue.popleft()
    x, y = t

    visited.append(t)
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 or dx != 0:
                ty = y + dy
                tx = x + dx
                if ty < 0 or tx < 0 or tx >= M or ty >= M:
                    continue
                if grid[ty][tx] == 0:
                    grid[ty][tx] = -999999999
                    bfs_queue.append([tx, ty])


# Form a 2D grid sum dp table so that we can check if some rectangle is valid
for y in range(M):
    for x in range(M):
        # this + left + up - top_left
        if x: grid[y][x] += grid[y][x-1] # left
        if y: grid[y][x] += grid[y-1][x] # up
        if 0 < y and 0 < x: grid[y][x] -= grid[y-1][x-1] # top_left

def dpSum(point):
    if point[0] < 0 or point[1] < 0:
        return 0
    return grid[point[1]][point[0]]

max_area = 0
for (a, b) in combinations(og, 2):
    x1, y1 = a
    x2, y2 = b
    # compress coordinates to a smaller space (index compression)
    x1 = uniqs.index(x1) + 1
    y1 = uniqs.index(y1) + 1
    x2 = uniqs.index(x2) + 1
    y2 = uniqs.index(y2) + 1
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    max_x = max(x1, x2)
    max_y = max(y1, y2)

    area_label_sum = dpSum((max_x, max_y)) \
                    - dpSum((min_x - 1, max_y)) \
                    - dpSum((max_x, min_y - 1)) \
                    + dpSum((min_x - 1, min_y - 1))
    
    if area_label_sum > 0:
        max_area = max(max_area, -~abs(a[1]-b[1]) * -~abs(a[0]-b[0]))

print(max_area)