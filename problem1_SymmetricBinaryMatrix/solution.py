import random
import time
import argparse

# random binary matrix generation
def generate_random_binary_matrix(rows, cols):
    matrix = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return matrix

# transpose of matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# calculate minimum insertions with cache 
def symmetric_matrix_cache(matrix, l, r, cache):
    if l >= r:
        if l == r:
            cache[(l,r)] = 0
            return cache[(l,r)]
        return 0
    if (l,r) in cache:
        return cache[(l,r)]
    if matrix[l] == matrix[r]:
        cache[(l,r)] = symmetric_matrix_cache(matrix, l+1, r-1, cache)
        return cache[(l,r)]
    if matrix[l] != matrix[r]:
        cache[(l,r)] = 1 + min(symmetric_matrix_cache(matrix, l+1, r, cache), symmetric_matrix_cache(matrix, l, r-1, cache))
        return cache[(l,r)]

# use cache to make insertions in matrix 
def generate_sym_matrix(matrix, cache):
    new_matrix = matrix[:]
    l, r = 0, len(matrix) - 1
    left = 0
    while l < r:
        if matrix[l] != matrix[r]:
            if cache[(l + 1, r)] < cache[(l, r - 1)]:
                new_matrix.insert(r+left+1, matrix[l])
                l += 1
            else:
                new_matrix.insert(l+left, matrix[r])
                left += 1
                r -= 1
        else:
            l += 1
            r -= 1

    return new_matrix

# returns min insertions and cache for row and columns insertions indices
def generate_insertion_cache(matrix):
    if not matrix:
        return 0
    m = len(matrix)
    cache_r = dict()
    rows_insertions = symmetric_matrix_cache(matrix, 0, m-1, cache_r)
    matrix_T = transpose_matrix(matrix)
    n = len(matrix_T)
    cache_c = dict()
    columns_insertions = symmetric_matrix_cache(matrix_T, 0, n-1, cache_c)
    print("Insertions - Rows and Columns: ", rows_insertions, columns_insertions)
    return rows_insertions + columns_insertions, cache_r, cache_c

# final symmetric matrix generation with minimum insertions
def main(args):
    rows, cols = args.rows, args.columns
    if not rows or not cols:
        print(f"Invalid Input Matrix with size: ({rows} x {cols})")
        return None
    matrix = generate_random_binary_matrix(rows, cols)
    print(f"Matrix of Size = ({rows}, {cols})")
    for row in matrix:
        print(row)
    s = time.time()
    insertions, row_cache, col_cache = generate_insertion_cache(matrix)
    print("Total #Insertions: ", insertions)
    new_matrix = generate_sym_matrix(matrix, row_cache)
    new_matrix = generate_sym_matrix(transpose_matrix(new_matrix), col_cache)
    new_matrix = transpose_matrix(new_matrix)
    print("Time taken in milliseconds:", round((time.time() - s)*1000, 5))
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(3,3))
        plt.imshow(new_matrix)
        plt.show()
    except:
        print(*new_matrix, sep='\n')

# main function for inputing #rows x #columns for test matrix. Deafult set to 5 x 5
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rows", type=int, default=5, help="input number of rows of a matrix")
    parser.add_argument("-c", "--columns", type=int, default=5, help="input number of rows of a matrix")
    args = parser.parse_args()
    main(args)
    