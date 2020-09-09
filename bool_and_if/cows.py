cow = int(input())
end_num = cow % 10
if 10 < cow < 20 or end_num == 0 or end_num == 5:
    print(cow, 'korov')
elif end_num == 6 or end_num == 7 or end_num == 8 or end_num == 9:
    print(cow, 'korov')
elif end_num == 1:
    print(cow, 'korova')
else:
    print(cow, 'korovy')
