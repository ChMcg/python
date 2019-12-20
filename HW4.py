#!/usr/bin/env python3
import re

def main():
    input_str = input("> ")
    res = [int(x) for x in re.findall('[-]?[0-9]+',input_str)]
    print(sum(res))

if __name__ == "__main__":
    main()
