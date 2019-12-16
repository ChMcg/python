#!/usr/bin/env python3

def remove_dublicates(somelist):
    assert isinstance(somelist, list)
    res = []
    for i in range(0, len(somelist)):
        if not somelist[i] in res:
            res.append(somelist[i])
    return res


def remove_empty(somelist):
    assert isinstance(somelist, list)
    while '' in somelist:
        somelist.remove('')

def main():
    s = input("> ")
    s = s.split(' ')
    # substr = list(dict.fromkeys(s))  
    # ^ shuffle values
    substr = s
    remove_empty(substr)
    substr = remove_dublicates(substr)
    print(' '.join(substr))

if __name__ == "__main__":
    main()