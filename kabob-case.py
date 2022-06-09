import argparse


def handleCase(toCase: str) -> str:
    newWord = "-".join(toCase.lower().split(" "))
    newWord = newWord[0].lower() + newWord[1:]
    return newWord


def main():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-s', '--toCase', type=str, nargs=1, help='')
    args = parser.parse_args()
    print(handleCase(args.toCase[0]))


if __name__ == '__main__':
    main()
