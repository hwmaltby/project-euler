#Henry Maltby 2017

def view(matrix):
    for line in matrix:
        print(*line, sep=", ")
    print("\n")

def minl_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    minl_matrix = [[0] * n for i in range(m)]
    for i in range(m):
        minl_matrix[i][0] = matrix[i][0] + minl_matrix[i - 1][0]
    for i in range(1, m):
        stable, k = False, 0
        while not stable:
            stable = True
            for j in range(n):
                if k == 0:
                    minl_matrix[j][i] = minl_matrix[j][i - 1] +\
                        matrix[j][i]
                    stable = False
                elif j != 0 and minl_matrix[j][i] > minl_matrix[j - 1][i] +\
                    matrix[j][i]:
                    minl_matrix[j][i] = minl_matrix[j - 1][i] + matrix[j][i]
                    stable = False
                elif j != m - 1 and minl_matrix[j][i] > minl_matrix[j + 1][i] +\
                    matrix[j][i]:
                    minl_matrix[j][i] = minl_matrix[j + 1][i] + matrix[j][i]
                    stable = False
            if i == 0:
                stable = True
            k += 1
    stable = False
    while not stable:
        stable = True
        for i in range(m):
            for j in range(n):
                #view(minl_matrix)
                if i != 0 and minl_matrix[j][i] > minl_matrix[j][i - 1] +\
                    matrix[j][i]:
                    minl_matrix[j][i] = minl_matrix[j][i - 1] + matrix[j][i]
                    stable = False
                elif i != n - 1 and minl_matrix[j][i] > minl_matrix[j][i + 1] +\
                    matrix[j][i]:
                    minl_matrix[j][i] = minl_matrix[j][i + 1] + matrix[j][i]
                    stable = False
                elif j != 0 and minl_matrix[j][i] > minl_matrix[j - 1][i] +\
                    matrix[j][i]:
                    minl_matrix[j][i] = minl_matrix[j - 1][i] + matrix[j][i]
                    stable = False
                elif j != m - 1 and minl_matrix[j][i] > minl_matrix[j + 1][i] +\
                    matrix[j][i]:
                    minl_matrix[j][i] = minl_matrix[j + 1][i] + matrix[j][i]
                    stable = False
    return minl_matrix[-1][-1]

f = open("problem_82_matrix.txt")
matrix = [line.split(',') for line in f.read().strip().split('\n')]
for i in range(len(matrix)):
    matrix[i] = [int(x) for x in matrix[i]]
print(minl_path_sum(matrix))

"""
    stable0, l = False, 0    
    while not stable0:
        stable0 = True
        for i in range(m):
            stable, k = False, 0
            while not stable:
                stable = True
                for j in range(n):
                    print(minl_matrix)
                    if k == 0 and l == 0:
                        minl_matrix[j][i] = minl_matrix[j][i - 1] +\
                            matrix[j][i]
                        stable = False
                    elif j != 0 and minl_matrix[j][i] > minl_matrix[j - 1][i] +\
                        matrix[j][i]:
                        minl_matrix[j][i] = minl_matrix[j - 1][i] + matrix[j][i]
                        stable = False
                    elif j != m - 1 and minl_matrix[j][i] > minl_matrix[j + 1][i] +\
                        matrix[j][i]:
                        minl_matrix[j][i] = minl_matrix[j + 1][i] + matrix[j][i]
                        stable = False
                    elif i != 0 and minl_matrix[j][i] > minl_matrix[j][i - 1] +\
                        matrix[j][i]:
                        minl_matrix[j][i] = minl_matrix[j][i - 1] + matrix[j][i]
                        stable0 = False
                    elif i != n - 1 and minl_matrix[j][i] > minl_matrix[j][i + 1] +\
                        matrix[j][i]:
                        minl_matrix[j][i] = minl_matrix[j][i + 1] + matrix[j][i]
                        stable0 = False
                if i == 0:
                    stable = True
                k += 1
        l += 1
"""