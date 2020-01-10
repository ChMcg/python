#!/usr/bin/env python3

"""
    Напишите программу, которая читает данные из файлов
    /etc/passwd и /etc/group на вашей системе и выводит
    следующую информацию в файл output.txt:
    1. Количество пользователей, использующих все имеющиеся
    интерпретаторы-оболочки.
    ( /bin/bash - 8 ; /bin/false - 11 ; ... )
    2. Для всех групп в системе - UIDы пользователей
    состоящих в этих группах.
    ( root:1, sudo:1001,1002,1003, ...)
"""

def main():
    passwd = open('/etc/passwd', 'r')
    groups = open('/etc/group', 'r')
    lines = passwd.readlines()
    temp = [x.strip().split(':')[6] for x in lines]
    interps = dict.fromkeys(temp, 0)
    for item in temp: 
        interps[item] += 1
    print('( {} )'\
        .format(" ; "\
        .join([str(x) + ' - ' + str(interps[x]) for x in interps.keys()])))
    
    

if __name__ == "__main__":
    main()