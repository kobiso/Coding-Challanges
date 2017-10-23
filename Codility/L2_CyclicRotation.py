def solution(A, K):
    # write your code in Python 2.7
    
    if len(A) == 0 or K == 0: # no shifting needed, exceptions
        return A
    
    else: # shifting needed
        shift = K - ((K / len(A)) * len(A)) # calculate minimum number of shifting times
        if shift == 0: return A # same array after shifting
        else: # not same array after shifting
            temp = list(A) # list copy
            for i in range(len(A)):
                newIndex = i + shift
                if i+shift >= len(A): # when out of index
                    newIndex = newIndex - len(A)                
                A[newIndex] = temp[i]
    return A