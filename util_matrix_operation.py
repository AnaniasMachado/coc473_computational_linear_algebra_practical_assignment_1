"""
Purpose: Store utility functions to be used by other programs.
"""

""" Libraries """

import math

from data_tasks_read import read_matrix_file, read_vector_file

""" Actual Code """

def gen_identity_matrix(n):
    I = []
    for i in range(0, n):
        row = [0 for j in range(n)]
        row[i] = 1
        I.append(row)
    return I

def copy_matrix(M):
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    T = []
    for i in range(len(M)):
        row = []
        for j in range(len(M)):
            row.append(M[i][j])
        T.append(row)
    return T

def copy_vector(M):
    T = [val for val in M]
    return T

def make_matrix(vectors_filepath):
    M = []
    for vector_filepath in vectors_filepath:
        vector = read_vector_file(vector_filepath)
        M.append(vector)
    return M

def print_matrix(M):
    for i in range(len(M)):
        print(M[i])

def matrix_vector_multiplication(A, B):
    if len(A[0]) != len(B):
        raise Exception("Error: Matrix-vector multiplication not defined for given matrix and vector.")
    n = len(A)
    p = len(B)
    row = []
    for i in range(n):
        val = 0
        for j in range(p):
            val += A[i][j] * B[j]
        row.append(val)
    return row

def matrix_matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        raise Exception("Error: Matrix-matrix multiplication not defined for given matrices.")
    n = len(A)
    m = len(B)
    p = len(B[0])
    C = []
    for i in range(n):
        row = []
        for j in range(p):
            val = 0
            for k in range(m):
                val += A[i][k] * B[k][j]
            row.append(val)
        C.append(row)
    return C

def apply_transpose(M):
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    n = len(M)
    for i in range(n):
        for j in range(i+1, n):
            temp = M[i][j]
            M[i][j] = M[j][i]
            M[j][i] = temp
    return M

def is_symmetric(M):
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    n = len(M)
    for i in range(0, n):
        for j in range(0, n):
            if M[i][j] != M[j][i]:
                return False
    return True

def is_diagonally_dominant(M):
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    n = len(M)
    for i in range(0, n):
        row_sum = 0
        col_sum = 0
        for j in range(0, n):
            if i != j:
                row_sum += math.fabs(M[i][j])
                col_sum += math.fabs(M[j][i])
        if (math.fabs(M[i][i]) < row_sum) or (math.fabs(M[i][i]) < col_sum):
            return False
    return True