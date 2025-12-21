f = lambda x: (x[:(k:=len(x)//2)]*2)==x

c=0
for s in input().split(","):
    a,b = map(int, s.split("-"))
    c+=sum(x for x in range(a, b+1) if f(str(x)))

print(c)