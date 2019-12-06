matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

for row in matrix:
    matrix_t = zip(*matrix)
# filter() map()

print('*' * 17)
for row in matrix_t:
    print(list(row))
matrix_t = zip(
    matrix[0],
    matrix[1],
    matrix[2],
    matrix[3],
    matrix[4])