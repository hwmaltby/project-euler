#Henry Maltby 2017

def minl_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += min(matrix[i][j - 1], matrix[i - 1][j])
    return matrix[-1][-1]

f = open("problem_81_matrix.txt")
matrix = [line.split(',') for line in f.read().strip().split('\n')]
for i in range(len(matrix)):
    matrix[i] = [int(x) for x in matrix[i]]
print(minl_path_sum(matrix))