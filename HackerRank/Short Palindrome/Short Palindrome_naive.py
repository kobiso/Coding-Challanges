# Time complexity: O(n^3)
#!/bin/python3

import sys
import string

def shortPalindrome(s):
    mod = pow(10,9)+7
    cnt = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                if s[j]==s[k]:
                    cnt += s[k+1:].count(s[i])

    return cnt % mod

if __name__ == "__main__":
    s = input().strip()
    result = shortPalindrome(s)
    print(result)
