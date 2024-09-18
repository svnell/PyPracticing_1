n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
summ_a, main_d, sub_d = 0, 0, 0
mirror = []
summ = []
fg = False

for i in range(n):
    mirror.extend([matrix[i][k] for k in range(n)])
if sorted(mirror) == [l for l in range(1, n*n + 1)]:
    fg = True

if fg:
    for i in range(n):
        for j in range(n):
            if j == i:
                main_d += matrix[i][j]
            if j == n - 1 - i:
                sub_d += matrix[i][j]
            summ_a += matrix[j][i]
        summ.append(summ_a)
        summ_a = 0
    for q in summ:
        if q != sub_d:
            fg = False

    print('YES' if fg and sub_d == main_d else 'NO')
else:
    print('NO')