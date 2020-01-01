#!/usr/bin/env python3

"""
    Встроенная функция input позволяет ожидать и возвращать данные из стандартного
    ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
    Используя данную функцию, напишите программу, которая:

    1. После запуска предлагает пользователю ввести неотрицательные целые числа,
    разделенные через пробел и ожидает ввода от пользователя.
    2. Находит наименьшее положительное число, не входящее в данный пользователем
    список чисел и печатает его.

    Например:

    -> 2 1 8 4 2 3 5 7 10 18 82 2
    6
"""

def get1(nums):
    assert isinstance(nums, list)
    i = 1
    while i in nums:
        i += 1
    return i

def get2(nums):
    assert isinstance(nums, list)
    b = [x for x in range(1, max(nums)) if x not in nums ]
    return b[0]

def main():
    input_str = input('>  ')
    nums = []
    try:
        nums = [int(x) for x in input_str.split()]
    except:
        print('please, use only numbers')
    print(get1(nums))
    
if __name__ == "__main__":
    main()
