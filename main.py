from typing import List

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def encrypt_caesar(message: str, key: int) -> str:
    global ALPHABET

    encrypted_message = ""

    for index, char in enumerate(message):
        encrypted_message += ALPHABET[(ALPHABET.index(char) + key) % 26]
    return encrypted_message


def make_table() -> List[List[str]]:
    global ALPHABET

    table: List[List[str]] = []

    for index, _ in enumerate(ALPHABET):
        row = [ALPHABET[letter] for letter in range(index, len(ALPHABET))]
        row += ALPHABET[0:index]

        table.append(row)

    return table


def encrypt_vigenere(decrypted_message: str, keyword: str) -> str:
    global ALPHABET
    encrypted_message = ""
    table = make_table()
    for message_index, message_letter in enumerate(decrypted_message):
        keyword_letter = keyword[message_index % len(keyword)]

        encrypted_letter = table[ALPHABET.index(keyword_letter)][ALPHABET.index(message_letter)]

        encrypted_message += encrypted_letter
    return encrypted_message


def decrypt_vigenere(encrypted_messge: str, keyword: str) -> str:
    """
    to get the n-th letter decrypted
    1. Find the row for the n-th letter in the keyword
    2. Get the index of the encryption letter from that row
    3. The decrypted letter will be ALPHABET[index]
    """
    global ALPHABET
    table = make_table()
    decrypted_message = ""

    for encrypted_index, encrypted_letter in enumerate(encrypted_messge):
        keyword_letter = keyword[encrypted_index % len(keyword)]
        keyword_row = table[ALPHABET.index(keyword_letter)]
        index_of_encrypted_letter = ord(encrypted_letter) - ord(keyword_letter)
        decrypted_message += ALPHABET[index_of_encrypted_letter]

    return decrypted_message


if __name__ == "__main__":
    encrypted_message = encrypt_vigenere("BLUEBLUEWINDOWSBEHINDTHESTARS", "MOOSE")
    print(f"Encrypted Message: {encrypted_message}")
    decrypted_message = decrypt_vigenere(encrypted_message, "MOOSE")
    print(f"Decrypted Message: {decrypted_message}")
