import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

get_input = lambda filename: [[int(x) for x in l.strip('\n').split(',')] for l in open(filename,'r+',encoding='utf-8').readlines()]

import math

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Largest area: {}'.format(part_one(inp)))

def part_one(corners: [[int]]) -> int:
    largestDistance, largestCorners = 0, []
    for i in range(len(corners)):
        for j in range(len(corners)):
            if euclidean_distance(corners[i], corners[j]) > largestDistance:
                largestDistance = euclidean_distance(corners[i], corners[j])
                largestCorners = [corners[i], corners[j]]
    return (abs(largestCorners[0][0] - largestCorners[1][0]) + 1) * (abs(largestCorners[0][1] - largestCorners[1][1]) + 1)

def euclidean_distance(cornerA: [int], cornerB: [int]) -> float:
    return math.sqrt((cornerA[0] - cornerB[0])**2 + (cornerA[1] - cornerB[1])**2)

if __name__ == "__main__":
    main()