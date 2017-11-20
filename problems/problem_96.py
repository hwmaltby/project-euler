#Henry Maltby 2017
import time

index = 0
answer = [0] * 50
asdf = 0

class Sudoku(object):

    def __init__(self, grid):
        self.grid = grid
        self.solvable = True
        self.solved = False
        self.possibilities = [[{} for i in range(9)] for j in range(9)]
        global asdf
        asdf += 1
        #print("starting.. " + str(asdf))
        self.update()
        #print(str(asdf) + " ..finished")
        asdf -= 1

    def find_value(self):
        a, b, val = 9, 9, 0
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    a, b = i, j
                    if len(self.possibilities[i][j]) == 1:
                        for num in self.possibilities[i][j]:
                            val = num
                            return a, b, val
        return a, b, val

    def update(self):
        #print(self.to_string())
        #time.sleep(0.7)
        self.update_possibilities()
        a, b, val = self.find_value()
        if val != 0 and self.solvable:
            self.grid[a][b] = val
            self.update()
        if val == 0:
            if a == 9:
                #print(self.to_string())
                #print("12h1f3jh23i1")
                global index
                global answer
                answer[index] = self.grid[0][0] * 100 + self.grid[0][1] * 10 + self.grid[0][2]
                self.solved = True
            else:
                #print("looking at " + str(a) + ", " + str(b))
                new_grid = [[i for i in x] for x in self.grid]
                for x in self.possibilities[a][b]:
                    #print("trying " + str(x))
                    new_grid[a][b] = x
                    attempt = Sudoku([[i for i in x] for x in new_grid])
                    #print(attempt.to_string())
                    #print(attempt.solvable)
                    if attempt.solvable:
                        self.grid = [[i for i in x] for x in attempt.grid]
                        #print("LOOK HERE")
                        #print(self.to_string())
                        if attempt.solved:
                            #print("this is 4513452t3i4345")
                            #print(self.solved)
                            #print(self.solvable)
                            break
                        self.update()

    def update_possibilities(self):
        poss = self.possibilities
        for i in range(9):
            a1, b1 = divmod(i, 3)
            good = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for j in range(9):
                a2, b2 = divmod(j, 3)
                test = self.grid[3 * a1 + a2][3 * b1 + b2]
                if test in good:
                    good.remove(test)
            for j in range(9):
                a2, b2 = divmod(j, 3)
                poss[3 * a1 + a2][3 * b1 + b2] = {i for i in good}
        for i in range(9):
            for j in range(9):
                test = self.grid[i][j]
                if test != 0:
                    for k in range(9):
                        if test in poss[i][k]:
                            poss[i][k].remove(test)
                        if test in poss[k][j]:
                            poss[k][j].remove(test)
        for i in range(9):
            for j in range(9):
                if len(poss[i][j]) == 0 and self.grid[i][j] == 0:
                    #print(str(i) + ", " + str(j))
                    self.solvable = False
        self.possibilities = poss

    def to_string(self):
        ans = ""
        for line in self.grid:
            ans += " ".join(map(str, line))
            ans += "\n"
        return ans

f = open("problem_96_sudoku.txt")
for i in range(50):
    f.readline()
    grid = [[] for j in range(9)]
    for j in range(9):
        grid[j] = [int(c) for c in f.readline().strip()]
    #print(i)
    sud = Sudoku(grid)
    index += 1
#print(answer)
print(sum(answer))