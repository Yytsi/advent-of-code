c=50
print(sum(((c:=(c+(ord(s[0])%4-1)*int(s[1:]))%(~9)**2)<1)for s in open(0)))