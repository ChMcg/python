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
    # id_s = dict.fromkeys([x.strip().split(':')[2] for x in lines], [])
    id_s = {}
    for i in lines:
        temp_p = i.strip().split(':')
        id_s[temp_p[0]] = temp_p[2]
    temp = [x.strip().split(':')[6] for x in lines]
    interps = dict.fromkeys(temp, 0)
    for item in temp: 
        interps[item] += 1
    print('( {} )'\
        .format(" ; "\
        .join([str(x) + ' - ' + str(interps[x]) for x in interps.keys()])))
    lines = groups.readlines()
    # group_names = [x.strip().split(':')[0] for x in lines]
    # group_users = dict.fromkeys(group_names, [])
    group_users = {}
    for item in lines:
        temp = item.strip().split(':')
        # group_names.append()
        if temp[3] != '':
            group_users[temp[0]] = temp[3].split(',')
    print('( {} )'\
        .format(', '\
        .join(['{}:{}'\
        .format(x, ','.join([id_s[name] for name in group_users[x]])) for x in group_users.keys()])))

    
    
    

if __name__ == "__main__":
    main()