#!/usr/bin/env python3

# https://projecteuler.net/problem=36
#---------------------------------------------------------------------------------------------------#
# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.                     #
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.  #
# (Please note that the palindromic number, in either base, may not include leading zeros.)         #
#---------------------------------------------------------------------------------------------------#

def is_palindromic_b10(num):
    str_num = str(num)
    length = len(str_num)
    for i in range(0, length // 2):
        if str_num[i] != str_num[length-i-1]:
            return False
    return True

def is_palindromic_b2(num):
    b_num = bin(num)[2:]
    length = len(b_num)
    for i in range(0, length // 2):
        if b_num[i] != b_num[length-i-1]:
            return False
    return True

def main():
    result = 0
    for num in range(0, 1_000_000):
        if is_palindromic_b10(num) and is_palindromic_b2(num):
            # print(f"{num} ", end='')
            result += num
    # print()
    print(f"{result}")
    
if __name__ == "__main__":
    main()
