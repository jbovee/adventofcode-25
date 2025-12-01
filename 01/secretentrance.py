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
        move = int(rot.replace('L','-').replace('R','+'))
        pos = (pos + move) % 100
        count += 1 if pos == 0 else 0
    return count

def part_two(inp):
    # starts at 50
    # number of times dial points at or passes 0
    count = 0
    pos = 50
    for rot in inp:
        move = int(rot.replace('L','-').replace('R','+'))
        count += move // (100 * int(move/abs(move)))
        count += int(pos != 0 and (pos + (move % -100)) <= 0) if move <= 0 else int(pos != 0 and (pos + (move % 100)) >= 100)
        pos = (pos + move) % 100
    return count

if __name__ == "__main__":
    main()