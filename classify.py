import openai
import pandas as pd
import json

# Open the input JSON file
with open('test1.json', 'r') as input_file:
    # Load the JSON data
    input_data = json.load(input_file)

# Open the output JSONL file
with open('output1.txt', 'w') as output_file:
    # Loop through each object in the input data
    for obj in input_data:
        # Write the object as a string to the output file
        output_file.write(json.dumps(obj) + '\n')