a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

if a1 > a2 and b1 > b2 and c1 > c2:
    warehouse = a1 * b1 * c1
    laptops = a2 * b2 * c2
    how_much_lap_in_warehouse = warehouse / laptops
    print(int(how_much_lap_in_warehouse))
else:
    print(0)