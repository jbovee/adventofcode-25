import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print(part_one(inp))

def part_one(inp: [str]) -> int:
    return sum([get_voltage(bank) for bank in inp])

def get_voltage(bank: str) -> int:
    batL, batLInd, batR = 0, 0, 0
    for i in range(len(bank) - 1):
        battery = int(bank[i])
        if battery > batL:
            batL = battery
            batLInd = i
    for j in range(batLInd + 1, len(bank)):
        battery = int(bank[j])
        if battery > batR:
            batR = battery
    return int('{}{}'.format(batL, batR))

if __name__ == "__main__":
    main()