"""
Purpose: Read the matrix and vector data files from the data folder.
"""

""" Libraries """

""" Actual Code """

def read_matrix_file(filepath):
    M = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.split()
            line = list(map(int, line))
            M.append(line)
    return M

def read_vector_file(filepath):
    M = []
    with open(filepath, "r") as f:
        line = f.readlines()
        line = [val.replace("\n", "").strip() for val in line]
        M = list(map(int, line))
    return M

