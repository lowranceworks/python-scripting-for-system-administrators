# #!/bin/python3

# BMI is Body Mass Index
# BMI = (weight in kg / height in meters sqaured)
# Imperial version: BMI * 703


def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are you measurements in metric or imperial units? ").lower().strip() # the strip function removes any white space from the beginning or end of the string  
    return (height, weight, system) # packs variables into tuple that will be unpacked later 

def calculate_bmi(weight, height, system='metric'): # sets a default value for the system argument
    """
    Return the Body Mass Index (BMI) for the given weight, height and measurement system.
    
    Args:
        weight ([type]): [description]
        height ([type]): [description]
        system (str, optional): [description]. Defaults to 'metric'.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info() # unpacks the tuple 
    if system.startswith('i'): # new method that checks the first character of the string \ substring -- if system == imperial would have worked as well   
        bmi = calculate_bmi(weight, system=system, height=height) # there are mutliple ways to call a function use positionally {not so safe, if the order of parameters is changed in a function this code breaks} -- (e.g. weight) or out of order {safer way} (e.g. system) -- if you use a keyword inside your function argument you have to continue to use keyword arugments (e.g  height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'): # if system == metric would have worked as well 
        bmi = calculate_bmi(weight, height) # system is not required, because the function defines system as 'metric' buy default 
        print(f"Your BMi is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")
