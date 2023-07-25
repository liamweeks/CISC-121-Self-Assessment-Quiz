"""
Write a function/value-returning method that takes two integer
parameters and returns the real value obtained by dividing the first parameter
by the second parameter. If the second parameter is 0, your function should
return 0.
"""

def fancy_division(a: int, b: int) -> float:
    if b == 0:
        return 0

    return a / b


if __name__ == "__main__":
    print(fancy_division(36, 0))
    print(fancy_division(81, 9))