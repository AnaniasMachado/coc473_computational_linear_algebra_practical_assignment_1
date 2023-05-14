"""
Purpose: Verify the results of the implemented algorithms for a set of matrix and vectors.
"""

""" Libraries """

import math
import random

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
    print("Computed matrix X with LU decomposition:")
    print_matrix(X)
    print("\n")

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)

    method = "Cholesky"
    X = linear_system_solver(A, B, method)
    print("Computed matrix X with Cholesky decomposition:")
    print_matrix(X)
    print("\n")

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)
    
    method = "Jacobi"
    X = linear_system_solver(A, B, method)
    print("Computed matrix X with Jacobi method:")
    print_matrix(X)
    print("\n")

    A = read_matrix_file(matrix)
    B = make_matrix(vectors)
    
    method = "Gauss-Seidel"
    X = linear_system_solver(A, B, method)
    print("Computed matrix X with Gauss-Seidel method:")
    print_matrix(X)
    print("\n")


    # Computing eigenvectors and eigenvalues

    M = read_matrix_file(matrix)
    
    method = "Power Method"
    eigenvectors, eigenvalues, determinant = eigenvector_eigenvalue_solver(M, method, determinant=True)
    print("Computed dominant eigenvector with Power Method:")
    print(eigenvectors)
    print("\n")

    print("Computed dominant eigenvalue with Power Method:")
    print(eigenvalues)
    print("\n")

    print("Computed determinant:")
    print(determinant)
    print("\n")

    M = read_matrix_file(matrix)
    
    method = "Jacobi Eigenvalue Algorithm"
    eigenvectors, eigenvalues, determinant = eigenvector_eigenvalue_solver(M, method, determinant=True)
    print("Computed matrix of eigenvectors with Jacobi Eigenvalue Algorithm:")
    print_matrix(eigenvectors)
    print("\n")

    print("Computed diagonal matrix of eigenvalues with Jacobi Eigenvalue Algorithm:")
    print_matrix(eigenvalues)
    print("\n")

    print("Computed determinant:")
    print(determinant)
    print("\n")