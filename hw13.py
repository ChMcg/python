#!/usr/bin/env python3.8

"""
    Напишите функцию, которая переводит значения показаний
    температуры из Цельсия в Фаренгейт и наоборот.
"""

def shift(a: float, type_from='c') -> float:
    type_from = type_from.lower()
    cel = ['c', 'cels', 'celsium']
    far = ['f', 'fah', 'fahrenheit']
    if type_from not in [*cel, *far]: 
        raise TypeError(f"unknown type_from '{type_from}'")
    if type_from in cel:
        return a * 9 / 5 + 32
    else:
        return (a - 32) * 5 / 9

def main():
    print('Test 1:', shift(shift(25), 'f')       == 25.0)
    print('Test 2:', shift(shift(25, 'C'), 'F')       == 25.0)
    print('Test 3:', shift(shift(30, 'c'), 'f')  == 30.0)
    print('Test 4:', shift(shift(50, 'f'), 'c')  == 50.0)
    print('Test 5:', shift(16, 'c')              == 60.8)

if __name__ == "__main__":
    main()