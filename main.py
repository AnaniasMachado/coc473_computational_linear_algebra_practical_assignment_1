"""
Purpose: Verify the results of the implemented algorithms for a set of matrix and vectors.
"""

""" Libraries """

import math
import random

from util_matrix_operation import get_transpose
from util_matrix_operation import matrix_matrix_multiplication
from util_matrix_operation import copy_matrix, copy_vector, make_matrix, print_matrix
from solvers import linear_system_solver
from solvers import eigenvector_eigenvalue_solver
from data_tasks_read import read_matrix_file, read_vector_file

""" Actual Code """

if __name__ == "__main__":
    matrix = "./data/Matriz_A.dat"
    vectors = ["./data/Vetor_B_01.dat", "./data/Vetor_B_02.dat", "./data/Vetor_B_03.dat"]

    # Solving a linear system

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)
    
    method = "LU"
    X = linear_system_solver(A, B, method)
    print(X)

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)

    method = "Cholesky"
    X = linear_system_solver(A, B, method)
    print(X)

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)
    
    method = "Jacobi"
    X = linear_system_solver(A, B, method)
    print(X)

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)
    
    method = "Gauss-Seidel"
    X = linear_system_solver(A, B, method)
    print(X)

    # Computing eigenvectors and eigenvalues

    M = read_matrix_file(matrix)
    
    method = "Power Method"
    eigenvectors, eigenvalues, determinant = eigenvector_eigenvalue_solver(M, method, determinant=True)
    print(eigenvectors)
    print(eigenvalues)
    print(determinant)

    M = read_matrix_file(matrix)
    
    method = "Jacobi Eigenvalue Algorithm"
    eigenvectors, eigenvalues, determinant = eigenvector_eigenvalue_solver(M, method, determinant=True)
    print_matrix(eigenvectors)
    print_matrix(eigenvalues)
    print(determinant)