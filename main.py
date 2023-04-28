import openai
import pandas as pd
import json

openai.api_key = "API KEY"
input_df = pd.read_csv('model_input.csv')
input_df = input_df.to_json(orient='records')
with open("test1.json", "w") as outfile:
    outfile.write(input_df)

