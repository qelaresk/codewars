
import matplotlib.pyplot as plt
import copy
# Implemented by Fatma Coskunfirat
# Link: https://www.codewars.com/kata/525fbff0594da0665c0003a3

def check_adjacent(matrix,i,j,N,M):
    live_cell = 0

    for row in range(i-1,i+2):
        if row < 0 or row >= N:
            continue
        for col in range(j-1,j+2):
            if col < 0 or col >= M:
                continue
            if matrix[row][col] == 1:
               live_cell += 1

    if matrix[i][j] == 1:
        live_cell -= 1

    return live_cell

def next_gen(cells):
    N = len(cells)
    if N == 0:
        return []
    M = len(cells[0])

    
    next_cell = copy.deepcopy(cells)

    for i in range(0,N):
        for j in range(0,M):
            my_result = check_adjacent(cells,i,j,N,M)
            if cells[i][j] == 1:
                if my_result < 2 or my_result > 3:
                     next_cell[i][j] = 0
            else:
                if my_result == 3:
                    next_cell[i][j] = 1
    return next_cell
    
# if __name__ == '__main__':
#     spiral = [[0,1,0],
#               [0,1,0],
#               [0,1,0]]

#     next_gen(spiral)

                












