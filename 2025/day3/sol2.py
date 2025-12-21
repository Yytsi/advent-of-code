def f(s, m, ready, dp):
    if s == "" or m < 1: return ""
    if (s,m) in ready: return dp[s][m]
    a = f(s[1:], m, ready, dp)
    b = int(s[0] + f(s[1:], m-1, ready, dp))
    dp[s] = dp.get(s, {})
    dp[s][m] = str(max(int(a) if a.isdigit() else 0, b))
    ready.append((s,m))
    return dp[s][m]

print(sum(int(f(input(), 12, [], {})) for x in"x"*200))