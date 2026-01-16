import sys


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    if len(sys.argv) == 1:
        sys.exit()
    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    if arg % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")


if __name__ == "__main__":
    main()
