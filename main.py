import pandas as pd
import json

df = pd.read_csv('observable/DIM_COMPANIES - DIM_COMPANIES.csv')

result = df.to_json(orient="records")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))

df.to_json("observable/export_df.json", orient="records")

