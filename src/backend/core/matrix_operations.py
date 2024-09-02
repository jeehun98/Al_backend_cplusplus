import matrix_operations

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# 행렬 덧셈
result_add = matrix_operations.matrix_add(A, B)
print("Matrix Addition Result:", result_add)

# 행렬 곱셈
result_multiply = matrix_operations.matrix_multiply(A, B)
print("Matrix Multiplication Result:", result_multiply)
