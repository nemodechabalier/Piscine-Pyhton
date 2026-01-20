from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate various statistics on given numbers"""
    numbers = list(args)

    for key, operation in kwargs.items():
        if len(numbers) == 0:
            print("ERROR")
            continue

        if operation == "mean":
            mean = sum(numbers) / len(numbers)
            print(f"mean : {mean}")

        elif operation == "median":
            sorted_nums = sorted(numbers)
            n = len(sorted_nums)
            if n % 2 == 0:
                median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
            else:
                median = sorted_nums[n // 2]
            print(f"median : {median}")

        elif operation == "quartile":
            sorted_nums = sorted(numbers)
            n = len(sorted_nums)
            q1 = sorted_nums[int(n * 0.25)]
            q3 = sorted_nums[int(n * 0.75)]
            print(f"quartile : [{float(q1)}, {float(q3)}]")

        elif operation == "std":
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            std = variance ** 0.5
            print(f"std : {std}")

        elif operation == "var":
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            print(f"var : {variance}")
