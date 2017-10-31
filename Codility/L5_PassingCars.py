def solution(A):
    # write your code in Python 2.7
    
    zero_count = 0 # the number of zero occurs
    passing_count = 0 # the number of car passing
    
    for i in range(len(A)):
        if A[i] == 0:
            zero_count = zero_count + 1
        else: # if A[i] == 1
            passing_count = passing_count + zero_count
            if passing_count > 1000000000: # exception point
                return -1
    
    return passing_count