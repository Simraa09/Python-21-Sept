rows = 5
num = 1

for i in range(rows, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()