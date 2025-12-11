import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Number of beam splits: {}'.format(part_one(inp)))

def part_one(manifold: [[str]]) -> int:
    laserIndices = set([manifold[0].index('S')])
    splits = 0
    for layer in manifold[1:]:
        if any([x != '.' for x in layer]):
            splitterIndices = [i for i in range(len(layer)) if layer[i] == '^']
            newLaserIndices = set()
            for laserIndex in laserIndices:
                if laserIndex in splitterIndices:
                    if (laserIndex - 1) > -1:
                        newLaserIndices.add(laserIndex - 1)
                    if (laserIndex + 1) < len(layer):
                        newLaserIndices.add(laserIndex + 1)
                    splits += 1
                else:
                    newLaserIndices.add(laserIndex)
                laserIndices = newLaserIndices
    return splits

if __name__ == "__main__":
    main()