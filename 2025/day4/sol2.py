M,c,h=140,0,{}
r,g=range(n:=M-2),h

for y in r:s = input();h|={y*M+x:46<ord(s[x])for x in r}
for k in r:
    for k in h: h[k]and sum(h.get((k//M+(4<j)-(j<3))*M+k%M+~((3^j)%~2),0)for j in r[:8])<4 and(g:=g|{k:0},c:=c+1)
    h = g

print(c)