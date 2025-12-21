f = lambda x: any((x[:l] * (len(x) // l)==x) for l in range(1, len(x) // 2 + 1))

c=0
for s in input().split(","):
    a,b = map(int, s.split("-"))
    c+=sum(x for x in range(a, b+1) if f(str(x)))

print(c)