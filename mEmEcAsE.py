import argparse


def handleCase(toCase: str) -> str:
    toCase = "".join(toCase.split(" "))
    newWord = ""
    i = 0
    for l in toCase:
        if i == 0:
            newWord += l.lower()
        else:
            newWord += l.upper()

        i = (i + 1) % 2

    return newWord


def main():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-s', '--toCase', type=str, nargs=1, help='')
    args = parser.parse_args()
    print(handleCase(args.toCase[0]))


if __name__ == '__main__':
    main()
