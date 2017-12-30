# Short answer code without using numpy

def productMatrix(A,B):

    # (i,j) * (j,k) = (i,k)
    if range(len(A[0])) != range(len(B)): # Matrix product is impossible
        return []
    
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

# Compile time: 24ms