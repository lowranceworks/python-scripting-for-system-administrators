# Basic Scripting

## Reading user input 

```
name = input("What is your name? ")
birthdate = input("What is your birthdate? ")
age = int(input("How old are you? "))

print(f"{name} was born on {birthdate}")
print(f"Half of your age is {age / 2}") 
```


## Function Basics
```
def hello_world():
    print('hello world')
```
see the function object: `hello_world` \
execute a function by calling it: `hello_world()` \
functions can accept arguments, you must define them in the parenthesis:
```
def print_name(name)
    print(f'Your name is {name}')
```

```
def add_two(num)
    return num + 2
```

## Using Functions in Scripts
see bmi.py 

## Using Standard Library Packages
The standard library comes with a lot of awesome functionality \
view the documentation [here](https://docs.python.org/3/library/index.html) \
review the time library documentation [here](https://docs.python.org/3/library/time.html#module-time) \

### reading the documentation
functions with sqaure brackets are [optional] \
functions with parenthesis are (required) \ 

### enter the repl and practice with the time library
store the localtime in a variable: `now = time.localtime` \
when you call `now` you'll receive a list of attributes inside the object you've created \ 
you can call any of these attributes with dot notation on the object `now.tm_year` \

## Working with Environment Variables
see running.py

## Interacting with Files

start a repl in the directory in the file you want to play with \ 
open the file to get started: `xmen_file = open('xmen_base.txt', 'r')` \

read the file by calling the read function on the new object: `xmen_file.read()` \ 
run the read function again, and you'll get an empty string \ 
this is because the 'seek' (also known as the cursor) is at the end of the file \ 
you can move the cursor back to the beginning with `xmen_file.seek(0)` \

```
>>> xmen_file.read()  
'Storm\nWolverine\nCyclops\nBishop\nNightcrawler'
>>> xmen_file.seek(6) 
6
>>> xmen_file.read()  
'\nWolverine\nCyclops\nBishop\nNightcrawler'
```

a file object is an iterable object \
to iterate through each line of a file, use a for loop: 
```
>>> for line in xmen_file:
...     print(line)
... 
Storm

Wolverine

Cyclops

Bishop

Nightcrawler
```

you can ignore the new line by adding the `end=""` argument
```
>>> for line in xmen_file:
...     print(line, end="")
... 
Storm
Wolverine
Cyclops
Bishop
Nightcrawler
```
when you're done with the file, close it! `xmen_file.close()` \




you can only interact with a file if it's open \
when you're done interacting with a file, you should close it \
.