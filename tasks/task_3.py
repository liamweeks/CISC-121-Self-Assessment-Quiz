"""
Write a function which takes a string (word) as an input parameter.
The function should print the complete word on the first line and
remove the last character on each successive line, ending with a
single (the first) character.

Example:

Input word: Test

Function output:

Test

Tes

Te

T
"""


def fancy_print(text: str):
    word_length = len(text)
    for char_index in range(0, word_length):
        print(text[0:(word_length - char_index)])


if __name__ == "__main__":
    fancy_print("Test")