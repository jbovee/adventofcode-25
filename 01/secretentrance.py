import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main():
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Door password is: {}'.format(part_one(inp)))
    print('Door password is actually: {}'.format(part_two(inp)))

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

def part_two(inp):
    # starts at 50
    # number of times dial points at or passes 0
    count = 0
    pos = 50
    for rot in inp:
        # print('pos: {}, rot: {}'.format(pos, rot))
        move = int(rot.replace('L','-').replace('R','+'))
        if rot[0] == 'L':
            count += move // -100
            if pos != 0:
                count += int((pos + (move % -100)) <= 0)
            pos = (pos + move) % -100
            if pos < 0:
                pos += 100
        elif rot[0] == 'R':
            count += move // 100
            if pos != 0:
                count += int((pos + (move % 100)) >= 100)
            pos = (pos + move) % 100
        # print('after| pos: {}, count: {}'.format(pos, count))
    return count

if __name__ == "__main__":
    main()