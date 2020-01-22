#!/usr/bin/env python3.8

"""
    Написать функцию Фиббоначи fib(n), которая вычисляет
    элементы последовательности Фиббоначи:
    1 1 2 3 5 8 13 21 34 55 ...
"""

def fib(n: int) -> int:
    if n < 2: return 1
    return fib(n-1) + fib(n-2)

def main():
    print('Test:', [fib(x) for x in range(0, 10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

if __name__ == "__main__":
    main()