a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 * b1 * c1 > a2 * b2 * c2:
    print('The first box is larger than the second one')
elif a1 * b1 * c1 < a2 * b2 * c2:
    print('The first box is smaller than the second one')
elif a1 * b1 * c1 == a2 * b2 * c2:
    print('Boxes are equal')
else:
    print('Boxes are incomparable')
