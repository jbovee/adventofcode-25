import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))
    database, ingredients = input_to_db(inp)
    testinp = get_input(os.path.join(cwd, 'test_input'))
    testDatabase, testIngredients = input_to_db(testinp)
    print('Fresh ingredients: {}'.format(part_one(database, ingredients)))

def part_one(database: [[int]], ingredients: [int]) -> int:
    return sum([int(any([ingredient in range(freshRange[0], freshRange[1] + 1) for freshRange in database])) for ingredient in ingredients])

def input_to_db(inp: [[str]]) -> ([[int]], [int]):
    atDbData = True
    database, ingredients = [], []
    for row in inp:
        if row and atDbData:
            database.append(list(map(int, row.split('-'))))
        elif row and not atDbData:
            ingredients.append(int(row))
        else:
            atDbData = False
    return (database, ingredients)

if __name__ == "__main__":
    main()