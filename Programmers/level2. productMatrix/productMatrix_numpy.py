# Answer code using numpy

import numpy as np

def productMatrix(A,B):

    # (i,j) * (j,k) = (i,k)
    if range(len(A[0])) != range(len(B)): # Matrix product is impossible
        return []
    
    return (np.matrix(A)*np.matrix(B)).tolist()

# Compile time: 170ms