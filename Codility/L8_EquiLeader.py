# Time complexity: O(n)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    candidate = None
    candidate_length = 0
    for i in range(len(A)):
        if candidate_length == 0:
            candidate_length += 1
            candidate = A[i]
        else:
            if candidate != A[i]:
                candidate_length -= 1
            else:
                candidate_length += 1
    
    num_leader = A.count(candidate)
    if num_leader <= len(A) // 2: return 0
    else: leader = candidate
    
    equi = 0
    leader_now = 0
    for i in range(0, len(A)-1):
        if leader == A[i]:
            leader_now += 1
        if leader_now > (i+1) // 2 and num_leader - leader_now > (len(A)-(i+1)) // 2:
            equi += 1
            
    return equi
        