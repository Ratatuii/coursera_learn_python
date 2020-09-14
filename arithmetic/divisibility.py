a, b = int(input()), int(input())
h1 = a % b
h1 = int(h1 / (h1 - 0.000001))
h2 = 1 - h1
sy = "YES"
sn = "NO"
print(h1 * sn, h2 * sy, sep='')
