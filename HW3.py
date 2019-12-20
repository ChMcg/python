#!/usr/bin/env python3

def get_stat(lst):
    assert isinstance(lst, list)
    ret = dict.fromkeys(lst, 0)         # 0 - default value
    for item in lst:
        ret[item] += 1
    return ret

def main():
    input_str = input("> ")
    substr = input_str.lower().split()
    d = get_stat(substr)
    max_value = max(d.values())
    result = []
    for item in list(d.items()):
        if item[1] == max_value:
            result.append(item)
    for res in result:
        print('{} - {}'.format(res[1], res[0]))
    

if __name__ == "__main__":
    main()