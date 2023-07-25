"""
Write a program that prompts the user for a word,
then prints the number of vowels this word contains.

(For this purpose, vowels are a,e,i,o,u.)
"""


def count_vowels(text_input: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_text_input = 0

    for char in text_input:
        if char in vowels:
            vowels_in_text_input += 1
    return vowels_in_text_input

if __name__ == "__main__":
    print(
        count_vowels(
            "scooby dooby doo"
        )
    )



