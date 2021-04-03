# #!/bin/python3
import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0') # stop and do what the action is


args = parser.parse_args()          # anything that happens after this, we should have our required arguments if provided

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:        # prints a specific error message (this is how you'll want to handle errors so you can have particular actions or messages for them)
    print(f"Error: {err}")
    sys.exit(2)
#except:                                 
#    print(f"")                         # prints any kind of error that you may receive (lazy way of handling errors)

else:
    with open(args.filename) as f:
        lines = f.readlines()           # returns each line as a list 
        lines.reverse()                 # lists have the ability to be reversed 

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])   # strips new line character, slice the -1 step value to reverse the string value (reverse a string)
finally:
    print("Finally")


# parse the arguments
# read the file, reverse the contents and print

