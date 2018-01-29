# Time complexity: O(n)
#!/bin/python3

import sys
import string


def shortPalindrome(input_string):
    c_dic = dict(zip(string.ascii_lowercase, range(26)))  # ascii value dict for every alphabet
    ip_ascii = [c_dic[i] for i in input_string]  # change input as ascii value
    one_c = [0] * 26  # for one character occurred (e.g. a)
    two_c = [[0] * 26 for _ in range(26)]  # for two chracter occurred (e.g. ab)
    thr_c = [0] * 26  # for three chracter occured following the rule (e.g. abb)
    total = 0

    for current in ip_ascii:
        # sum the number of matching palindrome when the last character is 'current' (e.g. abba)
        total += thr_c[current]
        for i in range(26):  # for every alphabet, sum the number of sequence such as 'abb'
            thr_c[i] += two_c[i][current]
        for i in range(26):  # for every alphabet, sum the number of sequence such as 'ab'
            two_c[i][current] += one_c[i]
        one_c[current] += 1  # Count the occurred character

    return total % (10 ** 9 + 7)


if __name__ == "__main__":
    s = input().strip()
    result = shortPalindrome(s)
    print(result)
