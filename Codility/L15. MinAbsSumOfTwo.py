# Python 3.6, Time complexity: O(nlog(n))
def solution(A):
    # Exception for only one element in the list A
    if len(A) == 1:
        return abs(A[0]+A[0])
    
    A.sort() # Sort the list
    
    # Seperate list A into two lists
    #   1. minus: list with minus sign integers
    #   2. plus: list with plus sign integers and zero
    minus, plus = [], []
    for i in range(len(A)):
        if A[i]<0:
            minus.append(A[i])
        else:
            plus.append(A[i])
    minus.reverse()
    
    # Exceptions
    if len(minus) == 0: # there is no minus sign
        return A[0]+A[0]
    if len(plus) == 0: # there is no plus sign
        return abs(A[-1]+A[-1])
        
    min_ = min(abs(minus[0]+minus[0]), plus[0]+plus[0]) # Initial min_
    right = 0
    # Compare plus and minus lists
    for i in range(len(plus)):
        while right < len(minus):
            if right-1 < 0 and right+1 < len(minus):
                right += 1
                continue
            elif abs(plus[i]+minus[right-1])>=abs(plus[i]+minus[right]) and right+1 < len(minus):
                right += 1
            else: # Stop when the min for 'i' is found
                right -= 1
                break
            
        # Check if it is min for until now
        if min_ > abs(plus[i]+minus[right]):
            min_ = abs(plus[i]+minus[right])
                
    return min_    