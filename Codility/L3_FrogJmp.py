# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 2.7
    
    if X >= Y: # does not have to jump
        return 0;
        
    else:
        range = Y-X
        if range % D == 0: # When the position equal to Y after jumps
            return range / D
        else: # When the position is greater than Y after jumps
            return (range / D) + 1