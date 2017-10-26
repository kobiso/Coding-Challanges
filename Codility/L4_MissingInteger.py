def solution(A):
    # write your code in Python 2.7
    
    max_integer = max(A)
    if max_integer <= 0:
        return 1
    else:
        counter = list([0]*(max_integer+1)) # Create counter list with length of A        
        for i in range(len(A)):
            if A[i] > 0:
                counter[A[i]] = counter[A[i]]+1
        
        zero_index = 0
        for j in range(len(counter)):
            if counter[max_integer-j] == 0 and max_integer != j:
                zero_index = max_integer-j      
                
        if zero_index == 0:
            return max_integer+1
        else:
            return zero_index           