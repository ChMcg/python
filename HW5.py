#!/usr/bin/env python3

def get1(nums):
    assert isinstance(nums, list)
    i = 1
    while i in nums:
        i += 1
    return i

def get2(nums):
    assert isinstance(nums, list)
    b = [x for x in range(1, max(nums)) if x not in nums ]
    return b[0]

def main():
    input_str = input('>  ')
    nums = []
    try:
        nums = [int(x) for x in input_str.split()]
    except:
        print('please, use only numbers')
    print(get1(nums))
    
if __name__ == "__main__":
    main()
