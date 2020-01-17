#!/usr/bin/env python3.8
from datetime import datetime
from functools import reduce
import typing
"""

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


def meas(s: str, func) -> None:
    start = datetime.now()
    print(f'{s}: {func()}')
    stop = datetime.now()
    print(f'Время: {stop - start}')


def main():
    # start = datetime.now()
    # print(f'p9: {problem9()}')
    # stop = datetime.now()
    # print(f'Время: {stop - start}')
    meas('Problem 9', problem9)
    meas('Problem 6', problem6)


if __name__ == "__main__":
    main()
