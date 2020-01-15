#!/usr/bin/env python3.8

"""
Problem 9:
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

def problem9() -> int:
    return [x for x in range(100) if x % 2 == 0]

def main():
    print(f'p9: {problem9()}')

if __name__ == "__main__":
    main()
