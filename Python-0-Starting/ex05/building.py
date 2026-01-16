import sys
import string


def count_text(text: str) -> dict:
    """
    Count upper letters, lower letters, punctuation,
     spaces, and digits in text.

    Parameters:
    - text (str): the string to analyze

    Returns:
    - dict: counts with keys 'upper', 'lower',
      'punct', 'space', 'digit', 'total'
    """
    counts = {'upper': 0, 'lower': 0, 'punct': 0, 'space': 0, 'digit': 0}
    for c in text:
        if c.isupper():
            counts['upper'] += 1
        elif c.islower():
            counts['lower'] += 1
        elif c.isdigit():
            counts['digit'] += 1
        elif c.isspace():
            counts['space'] += 1
        elif c in string.punctuation:
            counts['punct'] += 1
    counts['total'] = len(text)
    return counts


def print_counts(counts: dict) -> None:
    """
    Print the counts in the required format.

    Parameters:
    - counts (dict): dictionary returned by count_text
    """
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


def main():
    """Main function:
      handles command line arguments and prints text analysis."""
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")
#   print(count_text.__doc__)
    counts = count_text(text)
    print_counts(counts)


if __name__ == "__main__":
    main()
