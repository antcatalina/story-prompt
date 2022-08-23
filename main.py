import json
from exceptions import *

# Function to validate length of string inputs
def get_input(var):
    while True:
        try:
            x = str(input(var))
            if len(x) < 2: raise LengthTooShortError
            elif len(x) > 25: raise LengthTooLongError
            break
        except LengthTooShortError:
            print("Value must be at least two characters. Try again...")
        except LengthTooLongError:
            print("Value must be less than 25 characters. Try again...")

    return x

# Get our number from the user and perform validation
while True:
    try:
        number = int(input("NUMBER: "))
        if number < 1: raise NumberTooLowError
        if number > 99999: raise NumberTooHighError
        break
    except NumberTooLowError:
        print("NUMBER value must be greater than 0. Try again...")
    except NumberTooHighError:
        print("NUMBER value must be less than 100000. Try again...")
    except ValueError: 
        print("NUMBER value must be a valid integer.  Try again...")

# Get our strings from the user and validate with our get_input function
unit = get_input("UNIT_OF_MEASURE: ")
place = get_input("PLACE: ")
adj = get_input("ADJECTIVE: ")
noun = get_input("NOUN: ")

# Format our inputs into json data
data = {
    "number": number,
    "unit_of_measure": unit,
    "place": place,
    "adjective": adj,
    "noun": noun
}

# Open our local json file and add the newly input data
filename = 'inputs.json'
with open(filename, "r") as file:
    file_data = json.load(file)
file_data.append(data)
with open(filename, "w") as file:
    json.dump(file_data, file)

# Create our output string
output = f"One day Anna was walking her { number } { unit } commute to { place } and found a { adj } { noun } on the ground."

print(output)