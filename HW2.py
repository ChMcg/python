#!/usr/bin/env python3

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