A = int(input())
B = int(input())
N = int(input())
pie = (A * 100) + B
cost = pie * N
print(cost // 100, cost % 100)
