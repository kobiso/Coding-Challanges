# Recursive Digit Sum
#!/bin/python3

import sys

def digitSum(n, k):
    dig = int(n)
    while dig >= 10:
        dig_l = map(int, str(dig))
        dig = sum(dig_l)
        
    dig_f = dig * k
    while dig_f >= 10:
        dig_l = map(int, str(dig_f))
        dig_f = sum(dig_l)
    return dig_f
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print(result)