#!/usr/bin/env python3.8

"""
    Напишите функцию letters_range, которая ведет себя
    похожим на range образом, однако в качестве start и
    stop принимает не числа, а буквы латинского алфавита
    (в качестве step принимает целое число) и возращает
    не перечисление чисел, а список букв, начиная с
    указанной в качестве start, до указанной в качестве
    stop с шагом step (по умолчанию равным 1).

    Пример:
    >>>letters_range('b', 'w', 2)
    ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']

    >>>letters_range('a', 'g')
    ['a', 'b', 'c', 'd', 'e', 'f']

    >>>letters_range('g', 'p')
    ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

    >>>letters_range('p', 'g', -2)
    ['p', 'n', 'l', 'j', 'h']

    >>>letters_range('a','a')
    []
"""

def letters_range(a: str, b: str, h = 1) -> list:
    return [chr(x) for x in range(ord(a), ord(b), h)]

def main():
    print('Test 1:', letters_range('b', 'w', 2)     == ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v'])
    print('Test 2:', letters_range('a', 'g')        == ['a', 'b', 'c', 'd', 'e', 'f'])
    print('Test 3:', letters_range('g', 'p')        == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'])
    print('Test 4:', letters_range('p', 'g', -2)    == ['p', 'n', 'l', 'j', 'h'])
    print('Test 5:', letters_range('a','a')         == [])

if __name__ == "__main__":
    main()