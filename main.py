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
#C:\Users\eugen\Documents\project
# prompt = "You are looking to buy potential add-on companies for companies that are similar or have synergies with Solero Technologies. The following JSON is information of Solero Technologies.'" + portfolio_df + \
#     "'\n The following JSON contains a list of companies. Add another property for each of these companies and create a new JSON. The new property should contain a rating based on if the company would be a good potential add-on for Solero. The rating would be 1,2,3. 1 being not a good add-on company for Solero Technologies and 3 being a very good add-on company for Solero Technologies. '" + input_df + "'"
# response = openai.Completion.create(engine="davinci", prompt=prompt)
# with open("response.json", "w") as f:
#     # Write the response to the file
#     json.dump(response.choices[0].text, f)
