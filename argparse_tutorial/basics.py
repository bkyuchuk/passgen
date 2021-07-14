import argparse

parser = argparse.ArgumentParser(description="Tutorial About argparse")
# Adding a positional argument.
# parser.add_argument("echo", help="echo the string you use here.")

# Adding a positional argument with a type
parser.add_argument("square", help="display the square of a given number",
                    type=int)

# Adding an optional argument.
parser.add_argument("-v", "--verbosity", help="increase output verbosity",
                    action="count", default=0)
# Now --verbose is more of a flag that doesn't require a value after it.
# 'action=store_true' means that, if the option is specified, assign the value
# True to 'args.verbose'.
args = parser.parse_args()
answer = args.square ** 2

if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 = {answer}")
else:
    print(answer)
