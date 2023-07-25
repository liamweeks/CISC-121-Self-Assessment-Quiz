"""
Given a list (or array) of n floating-point numbers, write
a program which searches and outputs the largest number in the list.
"""
import random
from typing import List

def generate_list(number_of_elements: int, bounds: (int, int)) -> List[int]:
    unsorted_list = []

    for i in range(0, number_of_elements):
        unsorted_list.append(random.uniform(bounds[0], bounds[1]))
    return unsorted_list


def find_the_largest_element(unsorted_list: List[int]) -> int:
    largest_val = 0

    for element in unsorted_list:
        if element > largest_val:
            largest_val = element
    return largest_val


if __name__ == "__main__""":
    list = generate_list(10, (0, 100))
    largest_number = find_the_largest_element(list)

    print(largest_number)
    print(list)