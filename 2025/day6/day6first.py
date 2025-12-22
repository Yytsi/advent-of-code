from aocd import data
print(sum(eval(l[-1].join(l[:-1]))for l in zip(*(r.split()for r in data.split("\n")))))