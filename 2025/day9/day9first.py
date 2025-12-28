from aocd import data
from itertools import *
print(max(-~abs(a[1]-b[1]) * -~abs(a[0]-b[0]) for (a, b) in combinations([list(map(int, row.split(","))) for row in data.split("\n")], 2)))