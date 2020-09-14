n = int(input())
m = int(input())
k = int(input())

tmp1 = k / m
tmp2 = k / n
if ((tmp1 <= n and k % n == 0) or (tmp2 <= m and k % m == 0)):
    print("YES")
else:
    print("NO")
