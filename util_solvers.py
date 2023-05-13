"""
Purpose: Store requested utility functions for solvers.
"""

""" Libraries """
from util_matrix_operation import apply_transpose

from algorithms import lu_decomposition, forward_substitution_LU, backward_substitution
from algorithms import cholesky_decomposition, forward_substitution
from algorithms import jacobi_method, gauss_seidel_method
from algorithms import power_method, jacobi_eigenvalue_algorithm
from algorithms import compute_determinant, compute_determinant_jea

""" Actual Code """

def linear_system_solver_B_vector(LU, B, method):
    Y = forward(LU, B)
    X = backward(LU, Y)
    return X

def linear_system_solver_B_matrix(LU, B, method):
    n = len(B)
    X = []
    for i in range(n):
        if method == "LU":
            YS = forward_substitution_LU(LU, B[i])
            XS = backward_substitution(LU, YS)
            X.append(XS)
        elif method == "Cholesky":
            YS = forward_substitution(LU, B[i])
            LU = apply_transpose(LU)
            XS = backward_substitution(LU, YS)
            LU = apply_transpose(LU)
            X.append(XS)
        else:
            raise Exception("Error: Invalid method.")
    return X

def linear_system_solver_iter_B_vector(A, B, algorithm):
    X = algorithm(A, B)
    return X

def linear_system_solver_iter_B_matrix(A, B, algorithm):
    n = len(B)
    X = []
    for i in range(n):
        XS = algorithm(A, B[i])
        X.append(XS)
    return X

def lu_solver(A, B):
    B_vector = (type(B[0]) == int)
    A = lu_decomposition(A)
    if B_vector:
        X = linear_system_solver_B_vector(A, B, "LU")
        return X
    else:
        X = linear_system_solver_B_matrix(A, B, "LU")
        return X

def cholesky_solver(A, B):
    B_vector = (type(B[0]) == int)
    A = cholesky_decomposition(A)
    if B_vector:
        X = linear_system_solver_B_vector(A, B, "Cholesky")
        return X
    else:
        X = linear_system_solver_B_matrix(A, B, "Cholesky")
        return X

def jacobi_solver(A, B):
    B_vector = (type(B[0]) == int)
    if B_vector:
        X = linear_system_solver_iter_B_vector(A, B, jacobi_method)
        return X
    else:
        X = linear_system_solver_iter_B_matrix(A, B, jacobi_method)
        return X

def gauss_seidel_solver(A, B):
    B_vector = (type(B[0]) == int)
    if B_vector:
        X = linear_system_solver_iter_B_vector(A, B, gauss_seidel_method)
        return X
    else:
        X = linear_system_solver_iter_B_matrix(A, B, gauss_seidel_method)
        return X