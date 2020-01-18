#!/usr/bin/env python3.8
from datetime import datetime
from functools import reduce

"""
    Решить несколько задач из projecteuler.net

    Решения должны быть максимально лаконичными, и использовать list comprehensions.

    problem9 - list comprehension : one line
    problem6 - list comprehension : one line
    problem48 - list comprehension : one line
    problem40 - list comprehension
"""

def problem9() -> int:
    """
    Problem 9:
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a^2 + b^2 = c^2

        For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
    """
    return reduce(lambda x,y: x*y,
                  [(a,b,c) for c in range(1000) for b in range(c) for a in range(b) if a**2 == (c-b)*(c+b) and a + b + c == 1000][0])

def problem6() -> int:
    """
    Problem 6
        The sum of the squares of the first ten natural numbers is,

        1^2+2^2+...+10^2=385
        The square of the sum of the first ten natural numbers is,

        (1+2+...+10)^2=55^2=3025
        Hence the difference between the sum of the squares of the first ten natural numbers and
        the square of the sum is 3025−385=2640.

        Find the difference between the sum of the squares of the first one hundred natural
        numbers and the square of the sum.
    """
    return sum([x for x in range(100+1)])**2 - sum([x**2 for x in range(100+1)])

def problem48() -> int:
    """
    Problem 48
        The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
        Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
    """
    return int(str(sum([x**x for x in range(1,1000+1)]))[::-1][:10][::-1])

def problem40() -> int:
    """
    Problem 40
        An irrational decimal fraction is created by concatenating the positive integers:

        0.12345678910`1`112131415161718192021...

        It can be seen that the 12^th digit of the fractional part is 1.

        If d_n represents the n^th digit of the fractional part, find the value of the following expression.

        d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
    """
    # some = reduce(lambda x, y: x + str(y), [a for a in range(1_000_000)], "")
    # some = reduce(lambda x, y: x + [int(c) for c in y], [str(a) for a in range(1_000_000)], [])
    # some = reduce(lambda x, y: x + y, [[int(k) for k in str(a)] for a in range(1_000_000)], [])
    some = [[int(k) for k in str(a)] for a in range(1_000_000)]
    some = reduce(lambda x, y: x + y, some, [])
    return int(some[1]) * int(some[10]) * int(some[100]) * int(some[1000]) * int(some[10000]) * int(some[100000]) * int(some[1000000])

def meas(name: str, func) -> None:
    start = datetime.now()
    print(f'{name}: {func()}')
    stop = datetime.now()
    print(f'Время: {stop - start}')


def main():
    meas('Problem 9 ', problem9)
    meas('Problem 6 ', problem6)
    meas('Problem 48', problem48)
    meas('Problem 40', problem40)


if __name__ == "__main__":
    main()
