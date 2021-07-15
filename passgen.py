import argparse
from colorama import init, deinit, Fore, Style
from utils import create_password, save_password, copy_to_clipboard

# Initialize colorama.
init()

parser = argparse.ArgumentParser(
    prog="passgen",
    description="Simple Password Generator")

parser.add_argument("-v", "--version",
                    action="version",
                    version="%(prog)s 1.0.0")

parser.add_argument("-l", "--length",
                    help="length of the password",
                    type=int,
                    nargs="?",
                    default=8,
                    const=8,
                    metavar="number")

parser.add_argument("-s", "--save",
                    help="save password to passwords.txt",
                    action="store_true")

parser.add_argument("-nn", "--no-numbers",
                    help="remove numbers",
                    action="store_true")

parser.add_argument("-ns", "--no-symbols",
                    help="remove symbols",
                    action="store_true")

length, save, no_numbers, no_symbols = parser.parse_args().__dict__.values()

has_numbers = not no_numbers
has_symbols = not no_symbols

# Get the generated password.
generated_password = create_password(length=length,
                                     has_numbers=has_numbers,
                                     has_symbols=has_symbols)

# Save to file.
if save:
    save_password(generated_password)

# Copy the password to clipboard.
copy_to_clipboard(generated_password)

# Output generated password.
print(Fore.BLUE + "Generated password: " + Style.BRIGHT + generated_password)
print(Fore.YELLOW + "Password copied to clipboard.")

# Close colorama.
deinit()
