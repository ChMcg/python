#!/usr/bin/env python3.8

"""
    Встроенная функция input позволяет ожидать и возвращать данные из стандартного
    ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
    Используя данную функцию, напишите программу, которая:

    1. После запуска предлагает пользователю ввести текст.
    2. Проверяет и, если возможно, преобразовывает полученный текст в число,
    используя рекурсивную функцию.
    Если число четное - делит его на 2 и выводит результат.
    Если число нечетное - умножает на 3 и прибавляет 1.
    После чего ждет следующего ввода.
    3.При получении в качестве вводных данных 'cancel' завершает свою работу.
"""

def parse(number: str) -> int:
    try:
        res = int(number[::-1][:1])
    except ValueError:
        raise ValueError
    if number[:len(number)-1] == '': 
        return res
    return 10*parse(number[:len(number)-1]) + res

def main():
    while True:
        input_str = input('> ')
        if input_str == 'cancel':
            print('Bye')
            break

        num = 0
        try: 
            num = parse(input_str)
        except ValueError: 
            print('Не удалось преобразовать введённый текст в число')
            continue

        if num % 2 == 0: print(num // 2)
        else: print(num * 3 + 1)
    

if __name__ == "__main__":
    main()
