## Project

### Story Prompt Generator

One day Anna was walking her {{NUMBER}} {{UNIT_OF_MEASURE}} commute to {{PLACE}} and found a {{ADJECTIVE}} {{NOUN}} on the ground.

Write a command line application in any language that accepts a json string of key-value inputs for the template above. With valid input, the application sends to STDOUT the story using the inputs provided. For example, "One day Anna was walking her 2 mile commute to school and found a blue rock on the ground." The application stores a record of valid inputs locally in a file. For the template above, you can assume NUMBER to be numerical data and all other inputs to be strings containing spaces, special characters, etc. Set sensible string validations for length. Validate all inputs and handle validation errors gracefully.

Write a second command line application that sends to STDOUT statistics about the stored records, including the maximum and minimum values for numerical inputs, the most common responses for string inputs, and anything else you think might be relevant.

Instructions for installing and running your applications should be added to this README file.

## Instructions for running

Navigate to directory containing all project folders. The first command line application can be run by:
> python3 main.py

The program will ask the user for inputs.

The second command line application can be run by:
> python3 stats.py 

The program will display all relevant statistics for the user inputs
