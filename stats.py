import json
import statistics
from statistics import mode

numbers, units, places, adjectives, nouns = [], [], [], [], []

def most_common(List):
    return(mode(List))

# Open our json file that includes all user inputs and load the data
f = open('inputs.json')
data = json.load(f)
  
# Iterate through the data and add all inputs to lists
for i in range(len(data)):
    numbers.append(data[i]['number'])
    units.append(data[i]['unit_of_measure'])
    places.append(data[i]['place'])
    adjectives.append(data[i]['adjective'])
    nouns.append(data[i]['noun'])

# Variables for useful values
greatest = max(numbers)
least = min(numbers)
common_unit = most_common(units)
common_place = most_common(places)
common_adj = most_common(adjectives)
common_noun = most_common(nouns)

print("Largest number input: ", greatest)
print("Smallest number input: ", least)
print("Most common unit: ", common_unit)
print("Most common place: ", common_place)
print("Most common adjective: ", common_adj)
print("Most common noun: ", common_noun)

# Closing file
f.close()