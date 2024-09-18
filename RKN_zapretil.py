n = int(input())
oblast = []
for i in range(n):
    row = [int(j) for j in input().split()]
    for k in range(n):
        if k <= i <= n - 1 - k or k >= i >= n - 1 - k:
            oblast.append(row[k])
print(max(oblast))