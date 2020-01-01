#!/usr/bin/env python3

"""
    Встроенная функция input позволяет ожидать и возвращать данные из стандартного
    ввода в виде строк (весь введенный пользователем текст до нажатия им enter).
    Используя данную функцию, напишите программу, которая:

    1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
    слоги, числа или их комбинации, разделенные пробелом.
    2. Считывает строку с текстом, и разбивает его на элементы списка, считая
    пробел символом разделителя.
    3. Печатает этот же список элементов (через пробел), однако с удаленными
    дубликатами.

    Пример:
    -> asdfdsf324 ?3 efref4r4 23r(*&^*& efref4r4 a a bb ?3
    asdfdsf324 ?3 efref4r4 23r(*&^*& a bb
"""

def remove_dublicates(somelist):
    assert isinstance(somelist, list)
    res = []
    for i in range(0, len(somelist)):
        if not somelist[i] in res:
            res.append(somelist[i])
    return res

def main():
    s = input("> ")
    s = s.split()
    # substr = list(dict.fromkeys(s))  
    # ^ shuffle values
    substr = s
    substr = remove_dublicates(substr)
    print(' '.join(substr))

if __name__ == "__main__":
    main()