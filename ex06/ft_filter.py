print(filter.__doc__)
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
print(list(result))