import sys
import os

cwd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cwd)
sys.path.append(parent)

from common import get_input

def main() -> None:
    inp = get_input(os.path.join(cwd, 'input'))

if __name__ == "__main__":
    main()