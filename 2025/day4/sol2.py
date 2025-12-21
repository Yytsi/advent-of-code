M,c,h=140,0,{}
r,g=range(n:=M-2),h

for y in r:
    s = input()
    for x in r:h[y*M+x]=46<ord(s[x])
    
for k in r:
    for y in r:
        for x in r:
            if h[y*M+x]<1:continue
            t=sum(h.get((y+(4<j)-(j<3))*M+x+~((3^j)%~2),0)for j in r[:8])
            if t < 4: g[y*M+x] = 0; c += 1
    h = g

print(c)