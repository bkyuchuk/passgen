import argparse

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
parser.add_argument("-nn", "--no-numbers", help="remove numbers",
                    action="store_true")
parser.add_argument("-ns", "--no-symbols", help="remove symbols",
                    action="store_true")

length, save, numbers, symbols = parser.parse_args().__dict__.values()

