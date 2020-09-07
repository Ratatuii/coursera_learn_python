N = int(input())
N %= 86400
h = N // 3600
N -= (h * 3600)
m = N // 60
N -= (m * 60)
print(h, end=':')
print(int(m / 10), m % 10, sep='', end=':')
print(int(N / 10), N % 10, sep='')

