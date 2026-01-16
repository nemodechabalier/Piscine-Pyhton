import sys
from ft_filter import ft_filter


def filterstring(s: str, n: int):
    """
    Return a list of words from s that have a length greater than n.
    """
    words = s.split(" ")
    return ft_filter(lambda word: len(word) > n, words)


def main():
    """
    Main function: handle arguments and print filtered words.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    if not isinstance(s, str):
        raise AssertionError("the arguments are bad")
    result = filterstring(s, n)
    print(result)


if __name__ == "__main__":
    main()
