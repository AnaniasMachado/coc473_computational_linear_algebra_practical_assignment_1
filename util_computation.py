"""
Purpose: Store utility functions for algorithms.
"""

""" Libraries """

import math

""" Actual Code """

def compute_vector_residual(X0, X1):
    if (len(X0) != len(X1)):
        raise Exception("Error: Operation not defined for vectors of different dimensions.")
    num = 0
    den = 0
    n = len(X0)
    for i in range(n):
        try:
            num += math.pow((X1[i] - X0[i]), 2)
            den += math.pow(X1[i], 2)
        except Exception as e:
            Exception(f"Error: Solution diverged. The following error occured: {str(e)}")
    try:
        residual = math.sqrt(num) / math.sqrt(den)
        return residual
    except Exception as e:
        raise Exception(f"Error: Iteractive method failed. The following error occured: {str(e)}")

def vector_normalization_supremum_norm(M):
    sup = max(M)
    T = [val/sup for val in M]
    return T

def compute_scalar_residual(S0, S1):
    residual = 0
    try:
        residual = math.fabs(S1 - S0) / math.fabs(S1)
    except Exception as e:
        raise Exception(f"Error: Power Method failed. The following error occured: {str(e)}")
    return residual

def get_greatest_elem_position(M):
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix is not a square matrix.")
    n = len(M)
    i_max, j_max = 0, 1
    for i in range(0, n):
        for j in range(i+1, n):
            if math.fabs(M[i][j]) > math.fabs(M[i_max][j_max]):
                i_max = i
                j_max = j
    return i_max, j_max

def get_jea_cos_and_sin(M, X, i, j):
    # jea stands for jacobi eigenvalue algorithm
    if (len(M) != len(M[0])):
        raise Exception("Error: Given matrix M is not a square matrix.")
    if (len(X) != len(X[0])):
        raise Exception("Error: Given matrix X is not a square matrix.")
    phi = math.pi / 4
    if M[i][i] != M[j][j]:
        phi = (1/2) * math.atan(2*M[i][j]/(M[i][i] - M[j][j]))
    X[i][i] = math.cos(phi)
    X[i][j] = (-1) * math.sin(phi)
    X[j][i] = math.sin(phi)
    X[j][j] = math.cos(phi)
    return X