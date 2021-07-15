import random
import os
from colorama import init, deinit, Fore

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*_-+="


def create_password(length: int = 8,
                    has_numbers: bool = True,
                    has_symbols: bool = True) -> str:
    """
    Create a password with a given `length`
    (default is `8`) containing alpha characters. If set to `False`
    the password will neither contain numbers nor special symbols.

    :param length: The length of the password specified by the user.
    :param has_numbers: Whether the password should contain numbers.
    :param has_symbols: Whether the password should contain symbols.
    :return: The password str.
    """
    chars = ALPHA
    if has_numbers:
        chars += NUMBERS
    if has_symbols:
        chars += SYMBOLS
    return generate_password(length, chars)


def generate_password(length: int, chars: str) -> str:
    """
    Generate a password by creating a list of random numbers. Each random number
    represents an index from `chars`. For each index, get it's
    matching char and return a `str`.

    :param length: The length of the password provided by the user.
    :param chars: The characters used when generating the password.
    :return: A `str` representing the password.
    """
    password = ""
    char_indexes = random.sample(range(0, len(chars)), length)
    for index in char_indexes:
        password += chars[index]
    return password


def save_password(password: str) -> None:
    """
    Save the given password to a text file in the same directory,
    where the script was executed.

    :param password: The password to be saved.
    :return: True if the password was saved successfully, False otherwise.
    """
    # Initialize colorama.
    init()
    with open(os.path.join(os.getcwd(), "passwords.txt"),
              "a") as passwords_file:
        print(password, file=passwords_file)
    print(Fore.GREEN + "Password saved to passwords.txt")
    # Close colorama.
    deinit()
