import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

import re

get_input = lambda filename: [list(map(int,n.split('-'))) for n in open(filename,'r+',encoding='utf-8').readline().split(',')]

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Invalid IDs total: {}'.format(part_one(inp)))

def part_one(inp: list[list[int]]) -> int:
    total = 0
    for i in inp:
        s,e = i[0],i[1]
        while s <= e:
            if is_dbl(s):
                total += s
            s = get_next_dbl(s)
    return total

def is_dbl(num: int) -> bool:
    return False if len(str(num)) % 2 != 0 else bool(re.match(r'^(\d+)\1$', str(num)))

def get_next_dbl(num: int) -> int:
    if num < 0:
        return None
    strnum = str(num)
    if len(strnum) % 2 != 0:
        return int('1{}'.format('0' * (((len(strnum) + 1) // 2) - 1)) * 2)
    fh = int(strnum[:len(strnum) // 2])
    if int(str(fh) * 2) > num:
        return int(str(fh) * 2)
    return int(str(int(strnum[:len(strnum) // 2]) + 1) * 2)

def get_prev_dbl(num: int) -> int:
    if (num < 0) or (len(str(num)) < 2):
        return None
    strnum = str(num)
    if len(strnum) % 2 != 0:
        return int('9' * (len(strnum) - 1))
    fh = int(strnum[:len(strnum) // 2])
    if int(str(fh) * 2) < num:
        return int(str(fh) * 2)
    return int(str(int(strnum[:len(strnum) // 2]) - 1) * 2)

if __name__ == "__main__":
    main()