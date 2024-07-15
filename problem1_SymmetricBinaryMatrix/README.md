
---

# Symmetric Binary Matrix Generator

`Problem Statement:` Given a 2D binary image, you are allowed to insert columns and rows wherever you want in the image. Take the input image and make the minimum number of insertions in order to produce an output mage that is symmetric both along the X and Y axes. Return this output.

This repository provides a Python script that generates a random binary matrix and converts it into a symmetric binary matrix by making the minimum number of insertions. The script outputs the original matrix, the number of insertions required, the final symmetric matrix, and the time taken for the process.

## Features

- **Generate a Random Binary Matrix**: Create a matrix with random binary values (0 or 1) of specified dimensions.
- **Matrix Transposition**: Transpose the generated matrix.
- **Minimum Insertions Calculation**: Calculate the minimum number of row and column insertions required to make the matrix symmetric.
- **Symmetric Matrix Generation**: Generate a symmetric matrix by inserting rows and columns based on the calculated insertions.
- **Visual Representation**: Display the final symmetric matrix using Matplotlib (if available).

## Requirements

- Python 3.x
- Matplotlib (optional, for visual representation)

## Usage

### Command Line Arguments

- `-r`, `--rows`: Number of rows for the random binary matrix (default: 5).
- `-c`, `--columns`: Number of columns for the random binary matrix (default: 5).

### Example Command

```bash
python solution.py -r 5 -c 5
```

### Output

The script prints the following to the console:
- The original matrix.
- The number of row and column insertions required.
- The total number of insertions.
- The time taken to generate the symmetric matrix.
- The final symmetric matrix.

If Matplotlib is installed, the final symmetric matrix is displayed as an image.

## Functions

- `generate_random_binary_matrix(rows, cols)`: Generates a random binary matrix of given dimensions.
- `transpose_matrix(matrix)`: Returns the transpose of a given matrix.
- `symmetric_matrix_cache(matrix, l, r, cache)`: Helper function to calculate minimum insertions using caching.
- `generate_insertion_cache(matrix)`: Calculates the number of insertions required for rows and columns and returns the cache.
- `generate_sym_matrix(matrix, cache)`: Generates a symmetric matrix using the cache of minimum insertions.
- `main(args)`: Main function to execute the script, generate the matrix, calculate and make insertions, and display the results.

---
