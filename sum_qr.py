n = int(input())
l_sector = int()
r_sector = int()
u_sector = int()
d_sector = int()
for i in range(n):
    row = [int(j) for j in input().split()]
    for k in range(n):
        if k < i < n - 1 - k:
            l_sector += row[k]
        elif k > i > n - 1 - k:
            r_sector += row[k]
        elif k > i and i < n - 1 - k:
            u_sector += row[k]
        elif k < i and i > n - 1 - k:
            d_sector += row[k]
print(f'Верхняя четверть: {u_sector}')
print(f'Правая четверть: {r_sector}')
print(f'Нижняя четверть: {d_sector}')
print(f'Левая четверть: {l_sector}')
