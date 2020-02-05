#!/usr/bin/env python3.8

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
    id_s = dict(zip([x.strip().split(':')[0] for x in lines], [x.strip().split(':')[2] for x in lines]))
    temp = [x.strip().split(':')[6] for x in lines] # list of all interpretators
    interps = dict.fromkeys(temp, 0)
    for item in temp: 
        interps[item] += 1
    print('( {} )'\
        .format(" ; "\
        .join([str(x) + ' - ' + str(interps[x]) for x in interps.keys()])))
    lines = groups.readlines()
    group_users = {}    # store groups in format (group name, list of group users logins)
    for item in lines:
        temp = item.strip().split(':')
        group_users[temp[0]] = []
        if temp[0] in id_s.keys():
            group_users[temp[0]] += [temp[0],]
        if temp[3] != '': # if group users list isn't empty
            group_users[temp[0]] += temp[3].split(',')
    print('( {} )'\
        .format(', '\
        .join(['{}:{}'\
        .format(x, ','.join([id_s[name] for name in group_users[x]])) for x in group_users.keys()])))


if __name__ == "__main__":
    main()