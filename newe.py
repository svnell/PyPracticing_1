def rek(matrix, n, m, shift):
    counter = 0
    while counter < n:
        if counter % 2 == 0:
            for i in range(counter, n):
                for j in range(counter, m):
                    if i == 0 + counter // 2 or j == m - 1 - counter // 2:
                        matrix[i][j] += shift
                        shift += 1
                        #print(matrix[i][j])
                print(matrix[i], "check right")

        else:
            print(counter)
            for i in range(n - 1 - counter // 2, 0, -1):
                for j in range(m - 1 - counter % 2, -1, -1):
                    if i == n - 1 - counter // 2 or j == 0 + counter // 2:
                        matrix[i][j] += shift
                        shift += 1
                print(matrix[i], "check left")

        counter += 1

        #else:
        #    for i in range(n-1, counter, -1):
        #        for j in range(m - 1, counter, -1):
        #            if i == n - counter or j == counter - 1:
        #                matrix[i][j] += shift
        #                shift += 1


    return matrix



rows, columns = [int(num) for num in input().split()]
addition = 1
matritsa = [[int() for _ in range(columns)] for _ in range(rows)]

fin = rek(matritsa, rows, columns, addition)
