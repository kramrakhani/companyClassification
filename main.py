import openai
import pandas as pd
import json

openai.api_key = "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"
input_df = pd.read_csv('model_input.csv')
input_df = input_df.to_json(orient='records')
portfolio_df = pd.read_csv('solero.csv')
portfolio_df = portfolio_df.to_json(orient='records')
with open("test1.json", "w") as outfile:
    outfile.write(input_df)

