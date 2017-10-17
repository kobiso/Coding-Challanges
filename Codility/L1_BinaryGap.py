def solution(N):
    # write your code in Python 2.7
    
    bin_str = bin(N)[2:] # getting binary representation
    max_count = 0 # for the maximum binary gap    
    bin_count = 0 # for the each binary gap
      
    for i in range(len(bin_str)):
        if bin_str[i] == '1': # when the value of index 'i' is '1'
            if bin_count >= max_count: 
                max_count = bin_count
            bin_count = 0
        else: # when the value of index 'i' is '0'
            bin_count = bin_count + 1
            
        if i+1 == len(bin_str): # if it is the last index, return 'max_count'
            return max_count
        
    return max_count