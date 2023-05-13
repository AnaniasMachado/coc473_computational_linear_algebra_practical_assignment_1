"""
Purpose: Store implemented numerical linear algebra algorithms.
"""

""" Libraries """

import math
import random

from util_matrix_operation import is_diagonally_dominant, is_symmetric
from util_matrix_operation import gen_identity_matrix, copy_matrix, apply_transpose
from util_matrix_operation import matrix_matrix_multiplication, matrix_vector_multiplication

from util_computation import compute_vector_residual, compute_scalar_residual
from util_computation import vector_normalization_supremum_norm
from util_computation import get_greatest_elem_position, get_jea_cos_and_sin

""" Actual Code """

def lu_decomposition(M):
    # This algorithm overwrites the original matrix M with the LU decomposition
    # The 1's in the main diagonal of the L matrix are not stored
    n = len(M)
    for k in range(0, n):
        if M[k][k] == 0:
            Exception("Error: Pivot is zero.\n")
        for i in range(k+1, n):
            M[i][k] = M[i][k]/M[k][k]
        for j in range(k+1, n):
            for i in range(k+1, n):
                M[i][j] = M[i][j] - M[i][k] * M[k][j]
    return M

def cholesky_decomposition(M):
    # This algorithm overwrites the original matrix M with the matrix L^T of Cholesky decomposition
    # Note that the lower diagonal elements from the original matrix are not overwritten
    if not is_symmetric(M):
        raise Exception("Error: Given matrix is not symmetric.")
    n = len(M)
    for k in range(0, n):
        if M[k][k] == 0:
            Exception("Error: Pivot is zero. Given matrix is not symmetric and positive definite.\n")
        M[k][k] = math.sqrt(M[k][k])
        for i in range(k+1, n):
            M[i][k] = M[i][k] / M[k][k]
        for j in range(k+1, n):
            for i in range(j, n):
                M[i][j] = M[i][j] - M[i][k] * M[j][k]
    return M

def forward_substitution(A, B):
    # In this case matrix A is necessarily lower triangular
    n = len(A)
    X = [0 for i in range(n)]
    for j in range(0, n, 1):
        if A[j][j] == 0:
            Exception("Error: Pivot is zero.\n")
        X[j] = B[j] / A[j][j]
        for i in range(j+1, n):
            B[i] = B[i] - A[i][j] * X[j]
    return X

def forward_substitution_LU(A, B):
    # In this case matrix A is necessarily lower triangular
    # This code is to be used only with the LU matrix produced by the LU algorithm
    n = len(A)
    X = [0 for i in range(n)]
    for j in range(0, n, 1):
        if A[j][j] == 0:
            Exception("Error: Pivot is zero.\n")
        # X[j] = B[j] / A[j][j]
        X[j] = B[j]
        for i in range(j+1, n):
            B[i] = B[i] - A[i][j] * X[j]
    return X

def backward_substitution(A, B):
    # In this case matrix A is necessarily upper triangular
    n = len(A)
    X = [0 for i in range(n)]
    for j in range(n-1, -1, -1):
        if A[j][j] == 0:
            Exception("Error: Pivot is zero.\n")
        X[j] = B[j] / A[j][j]
        for i in range(0, j):
            B[i] = B[i] - A[i][j] * X[j]
    return X

def jacobi_method(A, B):
    if not is_diagonally_dominant(A):
        print("Warning: Given matrix is not diagonally dominant. Convergence may not be guaranteed.")
    tol = math.pow(10, -12)
    n = len(A)
    X = [random.uniform(tol, 1) for i in range(n)]
    while True:
        X_new = []
        for i in range(n):
            xi = B[i]
            for j in range(n):
                if i != j:
                    xi -= A[i][j] * X[j]
            xi = xi / A[i][i]
            X_new.append(xi)
        residual = compute_vector_residual(X, X_new)
        if residual < tol:
            return X_new
        else:
            X = X_new

def gauss_seidel_method(A, B):
    if not is_diagonally_dominant(A):
        print("Warning: Given matrix is not diagonally dominant. Convergence may not be guaranteed.")
    tol = math.pow(10, -12)
    n = len(A)
    X = [random.uniform(tol, 1) for i in range(n)]
    while True:
        X_new = []
        for i in range(n):
            xi = B[i]
            for j in range(0, i):
                xi -= A[i][j] * X_new[j]
            for j in range(i+1, n):
                xi -= A[i][j] * X[j]
            xi = xi / A[i][i]
            X_new.append(xi)
        residual = compute_vector_residual(X, X_new)
        if residual < tol:
            return X_new
        else:
            X = X_new

def power_method(M):
    tol = math.pow(10, -12)
    n = len(M)
    X = [random.uniform(tol, 1) for i in range(n)]
    X[0] = 1
    eigenvalue = 1
    while True:
        Y = matrix_vector_multiplication(M, X)
        new_eigenvalue = max(Y)
        X = vector_normalization_supremum_norm(Y)
        residual = compute_scalar_residual(new_eigenvalue, eigenvalue)
        if residual < tol:
            return X, new_eigenvalue
        else:
            eigenvalue = new_eigenvalue

def jacobi_eigenvalue_algorithm(M):
    if not is_symmetric(M):
        raise Exception("Error: Given matrix is not symmetric.")
    tol = math.pow(10, -12)
    n = len(M)
    X = gen_identity_matrix(n)
    i, j = get_greatest_elem_position(M)
    while math.fabs(M[i][j]) > tol:
        P = gen_identity_matrix(n)
        P = get_jea_cos_and_sin(M, P, i, j)
        X = matrix_matrix_multiplication(X, P)
        M = matrix_matrix_multiplication(M, P)
        M = matrix_matrix_multiplication(apply_transpose(P), M)
        i, j = get_greatest_elem_position(M)
    return X, M

def compute_determinant(M):
    LU = lu_decomposition(copy_matrix(M))
    n = len(M)
    determinant = 1
    for i in range(0, n):
        determinant *= LU[i][i]
    return determinant

def compute_determinant_jea(eigenvalues):
    n = len(eigenvalues)
    determinant = 1
    for i in range(0, n):
        determinant *= eigenvalues[i][i]
    return determinant