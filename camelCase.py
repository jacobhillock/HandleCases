import argparse
from PascalCase import handleCase as handlePascal


def handleCase(toCase: str) -> str:
    newWord = handlePascal(toCase)
    newWord = newWord[0].lower() + newWord[1:]
    return newWord


def main():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-s', '--toCase', type=str, nargs=1, help='')
    args = parser.parse_args()
    print(handleCase(args.toCase[0]))


if __name__ == '__main__':
    main()
