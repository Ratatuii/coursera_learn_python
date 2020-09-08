n = int(input())
m = int(input())
k = int(input())

chocolate = n * m
tmp = chocolate % k
if tmp == n or tmp == m:
    print('YES')
elif n == m and chocolate % n == 0 and k % 2 == 0 and chocolate - k > 0:
    print('YES')
else:
    print('NO')
