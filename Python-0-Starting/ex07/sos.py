import sys

NESTED_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/"
}


def encode_morse(s: str) -> str:
    """
    Encode a string into Morse code.
    """
    return " ".join(NESTED_MORSE[c] for c in s)


def main():
    """
    Main fonction take argv and print in morse
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    s = sys.argv[1]
    if not all(c.isalnum() or c.isspace() for c in s):
        raise AssertionError("the arguments are bad")
    s = s.upper()
    print(encode_morse(s))


if __name__ == "__main__":
    main()
