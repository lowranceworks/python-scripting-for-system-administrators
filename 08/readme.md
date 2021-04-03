# Intermediate Scripting

## Parsing Command Line Parameters
add flexibility to your scripts so that you can use them in other scripts \ 
review the sys module [here]() \ 
run the following commands in the repl:
```
`py.exe ./param.py testing`
`py.exe ./param.py testing testing123 'another test'`
`py.exe ./param.py` 
```
note that you can provide arguments are seperated by spaces, you can include an argument with spaces if you wrap it in single quotes. \  
you'll receive an error if you don't pass a paramter to this \
this is why you'll need something more robust, because people will use your scripts incorrectly 

**.**
```
.
```

## Robust CLIs with 'argparse' - part 1
the argparse module goes much further than the sys module's argv function \
[argparse module documentation](https://docs.python.org/3/library/argparse.html)
this module allows you to to define specific types or arguments, documentation for arguments and optional or required flags \
error checking is built into this module \
prompts the user when they're using the script wrong \ 
run the code below:
```
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()
print(args)
```
run `py.exe ./reverse_file.py fake.txt` \
run `py.exe ./reverse_file.py` to see an error \
run `py.exe ./reverse_file.py -h` to view help info that you defined \

now add two lines of code to the script:
```
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0') # stop and do what the action is
```
you've defined optional arguments, try them out
`py.exe .\reverse_file.py --version` \


## Robust CLIs with 'argparse' - part 2 
.
**.**
```
.
```

## Handling Errors with try/expect/else/finally
if you try to reverse a file that doesn't exist, you will receive a traceback error \
let's eliminate this error \ 
this is where we learn about exception handling \
use except with the actually error you plan on receiving \
finally happens everytime, useful if there's some cleanup that needs to happen every single time the script runs

```
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:        # prints a specific error message (this is how you'll want to handle errors so you can have particular actions or messages for them)
    print(f"Error: {err}")
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
```

## Exit statues
right now, if an error occurs the exit status is 0 (traditionally 0 is a passing status) \
we want to exit with a different status, because if we use this script with another script, an error will occur and the script will continue as the exit status is 0 \ 

**.**
```
import sys
...
sys.exit(2)
```

## Execute Shell Commands from Python
.
**.**
```
.
```

## Advanced Iteration with List Comprehensions 
.
**.**
```
.
```
