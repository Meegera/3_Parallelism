import numpy as np
from multiprocessing import Pool

def write(matrix):
    #import numpy as np
    matrix = np.array(matrix).reshape(len(reader_matrix(1)), len(reader_matrix(2)[1]))
    with open('result.txt', 'a') as f:
        f.write(str(matrix) + " ")

def multiplication(x, y):
    return sum(i*k for i, k in zip(x, y))

def reader_matrix(number):
    matrix = []
    with open(f'matrix{number}', 'r') as f:
        for line in f.readlines():
            matrix.append(list(map(int, line.split(', '))))
    return matrix


if name == 'main':
     with Pool(processes=4) as pool:
          matrix = pool.starmap(multiplication, [(i, k) for i in reader_matrix(1) for k in zip(*reader_matrix(2))])
          write(matrix)