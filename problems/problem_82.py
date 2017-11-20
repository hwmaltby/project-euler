#Henry Maltby 2017

def minl_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    minl_matrix = [[0] * n for i in range(m)]
    for i in range(m):
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
    return min([minl_matrix[i][-1] for i in range(m)])

f = open("problem_82_matrix.txt")
matrix = [line.split(',') for line in f.read().strip().split('\n')]
for i in range(len(matrix)):
    matrix[i] = [int(x) for x in matrix[i]]
print(minl_path_sum(matrix))