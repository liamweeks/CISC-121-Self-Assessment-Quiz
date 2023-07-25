"""
Write a function isEven, which evaluates if a given integer
number (given as a parameter for the function) is an even number.
The function should return a Boolean value True if the number is
even and False if the number is odd.

Given a list (or array) of n integer numbers, write a program
which uses the function isEven to determines the number of even items in the list.
"""
import random
from typing import List

def isEven(number_to_check: int) -> bool:
    return number_to_check % 2 == 0


def generate_list(number_of_elements: int, bounds: (int, int)) -> List[int]:
    unsorted_list = []

    for i in range(0, number_of_elements):
        unsorted_list.append(random.randrange(bounds[0], bounds[1]))
    return unsorted_list


if __name__ == "__main__":
    number_of_even_elements = 0
    unsorted_list = generate_list(10, (0, 100))

    for element in unsorted_list:
        if isEven(element):
            number_of_even_elements += 1
    print(f"{number_of_even_elements}")
    print(f"{unsorted_list}")
