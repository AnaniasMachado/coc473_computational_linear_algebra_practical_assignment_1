"""
Purpose: Store requested solvers.
"""

""" Libraries """
from util_solvers import lu_solver, cholesky_solver, jacobi_solver, gauss_seidel_solver
from algorithms import power_method, jacobi_eigenvalue_algorithm
from algorithms import compute_determinant, compute_determinant_jea

""" Actual Code """

def linear_system_solver(A, B, method):
    if (len(A) != len(A[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    if method == 'LU':
        X = lu_solver(A, B)
        return X
    elif method == 'Cholesky':
        X = cholesky_solver(A, B)
        return X
    elif method == 'Jacobi':
        X = jacobi_solver(A, B)
        return X
    elif method == 'Gauss-Seidel':
        X = gauss_seidel_solver(A, B)
        return X
    else:
        raise Exception("Error: Invalid method.")

def eigenvector_eigenvalue_solver(M, method, determinant=False):
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    det = 0
    if method == 'Power Method':
        if determinant:
            det = compute_determinant(M)
        eigenvector, eigenvalue = power_method(M)
        if determinant:
            return eigenvector, eigenvalue, det
        return eigenvector, eigenvalue
    elif method == 'Jacobi Eigenvalue Algorithm':
        eigenvectors, eigenvalues = jacobi_eigenvalue_algorithm(M)
        if determinant:
            det = compute_determinant_jea(eigenvalues)
            return eigenvectors, eigenvalues, det
        return eigenvectors, eigenvalues
    else:
        raise Exception("Error: Invalid method.")