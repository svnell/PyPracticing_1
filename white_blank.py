n, m = [int(num) for num in input().split()]
row = str()
for i in range(1,  n+1):
    for j in range(m):
        row += str(i + j * n)+' '
    print(row.ljust(3))
    row = str()
