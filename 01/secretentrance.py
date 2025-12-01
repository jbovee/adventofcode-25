import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main():
    inp = get_input(os.path.join(cwd, 'input'))
    print('Door password is: {}'.format(part_one(inp)))

def part_one(inp):
    # starts at 50
    # number of times dial is left pointing at 0 after any rotation in the sequence
    count = 0
    pos = 50
    for rot in inp:
        # print('pos: {}, rot: {}'.format(pos, rot))
        if rot[0] == 'L':
            pos = (pos - (int(rot[1:]) % 100) + 100) % 100
        elif rot[0] == 'R':
            pos = (pos + (int(rot[1:]) % 100)) % 100
        if pos == 0:
            count += 1
        # print('after| pos: {}'.format(pos))
    return count

if __name__ == "__main__":
    main()