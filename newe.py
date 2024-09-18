n = int(input())
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
res = [[0 for q in range(n)] for w in range(n)]
reslt = 0
mirror = matrix1

for _ in range(int(input()) - 1):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mirror[i][k] * matrix1[k][j]
    mirror = res
    res = [[0 for q in range(n)] for w in range(n)]


for _ in range(n):
    print(*mirror[_])