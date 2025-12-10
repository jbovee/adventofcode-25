import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

import re

get_input = lambda filename: [re.sub(r' +', r' ', l.strip('\n')).strip().split(' ') for l in open(filename,'r+',encoding='utf-8').readlines()]

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Worksheet grand total: {}'.format(part_one(inp)))

def part_one(worksheet: [[str]]) -> int:
    return sum([eval(worksheet[-1][i].join([symbolRow[i] for symbolRow in worksheet[:-1]])) for i in range(len(worksheet[-1]))])

if __name__ == "__main__":
    main()