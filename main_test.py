""" Libraries """

import math
import random

from util_matrix_operation import get_transpose
from util_matrix_operation import matrix_matrix_multiplication
from solvers import linear_system_solver
from solvers import eigenvector_eigenvalue_solver
from data import ts00, ts01

""" Actual Code """

def print_matrix(M):
    for i in range(len(M)):
        print(M[i])

def copy_matrix(M):
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

if __name__ == "__main__":
    # Solving a linear system
    # """
    A = copy_matrix(ts00["A"])
    B = copy_vector(ts00["B"])
    
    method = "LU"
    X = linear_system_solver(A, B, method)
    # print_matrix(A)
    print(X)

    A = copy_matrix(ts01["A"])
    B = copy_vector(ts01["B"])

    method = "Cholesky"
    X = linear_system_solver(A, B, method)
    print_matrix(A)
    print(X)
    C = matrix_matrix_multiplication(A, get_transpose(A))
    print_matrix(C)

    A = copy_matrix(ts00["A"])
    B = copy_vector(ts00["B"])
    
    method = "Jacobi"
    X = linear_system_solver(A, B, method)
    print(X)

    A = copy_matrix(ts00["A"])
    B = copy_vector(ts00["B"])
    
    method = "Gauss-Seidel"
    X = linear_system_solver(A, B, method)
    print(X)
    # """

    # Computing eigenvectors and eigenvalues
    """
    M = copy_matrix(ts00["A"])
    
    method = "Power Method"
    eigenvectors, eigenvalues, determinant = eigenvector_eigenvalue_solver(M, method, determinant=True)
    print(eigenvectors)
    print(eigenvalues)
    print(determinant)

    M = copy_matrix(ts00["A"])
    
    method = "Jacobi Eigenvalue Algorithm"
    eigenvectors, eigenvalues, determinant = eigenvector_eigenvalue_solver(M, method, determinant=True)
    print_matrix(eigenvectors)
    print_matrix(eigenvalues)
    print(determinant)
    """