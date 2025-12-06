import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

get_input = lambda filename: [[c for c in l.strip('\n')] for l in open(filename,'r+',encoding='utf-8').readlines()]

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Accessible rolls: {}'.format(part_one(inp)))

def part_one(inp: [[str]]) -> int:
    accessible = 0
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == '@':
                neighbors = 0
                directions = [(row - 1, col), (row - 1, col + 1), (row, col + 1), (row + 1, col + 1), (row + 1, col), (row + 1, col - 1), (row, col - 1), (row - 1, col - 1)]
                for direction in directions:
                    if (direction[0] > -1) and (direction[1] > -1) and (direction[0] < len(inp)) and (direction[1] < len(inp[row])) and inp[direction[0]][direction[1]] == '@':
                        neighbors += 1
                if neighbors < 4:
                    accessible += 1
    return accessible

if __name__ == "__main__":
    main()