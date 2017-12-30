# Answer code without using numpy

def productMatrix(A,B):
    answer = [] # define return variable
    
    # (i,j) * (j,k) = (i,k)
    if range(len(A[0])) != range(len(B)): # Matrix product is impossible
        return answer
    
    for i in range(len(A)):
        column=[]
        for k in range(len(B[0])):
            sum = 0
            for j in range(len(A[0])):
                sum += A[i][j]*B[j][k]
            column.append(sum)
        answer.append(column)
    return answer

# Compile time: 23ms