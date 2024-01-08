"""
Write a program that reads and integer from the User
and then prints out  the number of factors that integer has.

For example, if the integer is 12, then the function would return 6,
since 12 divides by 1, 2, 3, 4, 6, 12

If x % y == 0, y is a factor of x.
"""
from typing import List, Set, Union
import math


def inefficient_factors(number: int) -> List[int]:
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def more_efficient_factor(number_to_factor: int) -> List[int]:
    factors = []

    for i in range(1, int(math.sqrt(number_to_factor))):  # Factors will always be less than the sqrt of a number
        if number_to_factor % i == 0:
            factors.append(i)
            factors.append(number_to_factor / i)
            # Since 'i' is a factor, divide number_to_factor by 'I'. Guaranteed to be a factor

    return factors


if __name__ == "__main__":
    # factors_of_one_billion_inefficient = inefficient_factors(1_000_000_000)  # Elapsed Time: 26.894s (98% CPU)
    factors_of_one_billion_more_efficient = more_efficient_factor(1_000_000_000)  # Elapsed Time: 0.02s (47% CPU)

    print(len(factors_of_one_billion_more_efficient))
