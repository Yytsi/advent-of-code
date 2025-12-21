c,a=50,0
for s in open(0):exec("a+=(c:=(c+ord(s[0])%4-1)%100)<1;"*int(s[1:]))
print(a)