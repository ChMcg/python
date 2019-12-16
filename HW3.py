#!/usr/bin/env python3
from HW2 import remove_empty

def get_stat(lst):
    assert isinstance(lst, list)
    ret = dict.fromkeys(lst, 0)
    for item in lst:
        ret[item] += 1
    return ret

def find_max(d):
    # assert isinstance(d, dict_items)
    lst = list(d)
    print(lst)
    max = lst[0]
    for item in lst:
        if item[1] > max[1]:
            max = item
    return max

def main():
    input_str = input("> ")
    input_str.lower()
    substr = input_str.split(' ')
    remove_empty(substr)
    # d = dict.fromkeys(substr)
    d = get_stat(substr)
    max_value = max(d.values())
    print(d)
    

if __name__ == "__main__":
    main()