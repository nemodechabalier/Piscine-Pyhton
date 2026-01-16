import os
from time import sleep


def ft_tqdm(lst: range):
    """Minimalist tqdm generator using only allowed functions."""
    total = len(lst)
    term_width = os.get_terminal_size().columns
    bar_width = term_width - 30
    if bar_width < 10:
        bar_width = 10

    for i, elem in enumerate(lst, start=1):
        percent = i / total
        filled = int(bar_width * percent)
        if filled < bar_width:
            bar = "=" * filled + ">" + " " * (bar_width - filled - 1)
        else:
            bar = "=" * bar_width

        print(f"\r{int(percent * 100):3}%|[{bar}]|{i}/{total}",
              end="", flush=True)
        yield elem

    print()


def main():
    """
    Main function for local testing of ft_tqdm.
    """
    for _ in ft_tqdm(range(333)):
        sleep(0.005)


if __name__ == "__main__":
    main()
