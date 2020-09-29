m = 0
while True:
    n = int(input())
    if n > m:
        m = n
    elif n == 0:
        print(m)
        break
