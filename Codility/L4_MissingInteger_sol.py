def solution(A):
    # write your code in Python 2.7
    
    '''
    We can only consider N integers as we are tying to find the smallest positive integer.    
    '''
    
    occur = [False]*len(A)
    
    for value in A: # Save occured positive integer less than N
        if 0 < value <= len(A):
            occur[value-1] = True
        
    for i in range(len(occur)): # Check the smallest positive integer
        if occur[i] == False:
            return i+1
    
    return len(occur)+1 # All positive integer less than N exist, so next integer is the answer