from aocd import data
g=data.split("\n")
p=e=""
m,c=[],0
for x in range(len(g[0])):
    s="".join(g[y][x]for y in range(len(g)))
    p=p or s[-1]
    exec((s.strip()=="")*"e+=p.join(m)+'+';p='';m=[];"or"m+=[s[:-1]];")
print(eval(e+p.join(m)))