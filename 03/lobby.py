import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    testinp = get_input(os.path.join(cwd, 'test_input'))
    print('Output joltage: {}'.format(part_one(inp)))
    print('Actual output joltage: {}'.format(part_two(inp)))

def part_one(inp: [str]) -> int:
    return sum([get_joltage(bank) for bank in inp])

def part_two(inp: [str]) -> int:
    return sum([get_big_joltage(bank) for bank in inp])

def get_joltage(bank: str) -> int:
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

def get_big_joltage(bank: str) -> int:
    batteryInds = list(range(len(bank) - 12, len(bank)))
    leftmost = -1
    for i in range(len(batteryInds)):
        if (i > 0) and ((batteryInds[i] - 1) == batteryInds[i - 1]):
            break
        for j in reversed(range(leftmost + 1, batteryInds[i])):
            if int(bank[j]) >= int(bank[batteryInds[i]]):
                batteryInds[i] = j
                leftmost = j
    return int(''.join([bank[x] for x in batteryInds]))

def show_bank_battery(bank: str, batteryInds: [int]) -> None:
    print(bank)
    temp = bank
    for d in range(len(temp)):
        if d not in batteryInds:
            temp = temp[:d] + ' ' + temp[d + 1:]
    print(temp)
    print(int(''.join([bank[x] for x in sorted(batteryInds)])))

if __name__ == "__main__":
    main()