import os
import pandas as pd

INPUT_FILE = "data.csv"
OUTPUT_FILE = "dist/data.js"
data = pd.read_csv(INPUT_FILE, names=["State", "County", "Cases", "Deaths"]).fillna('')
data["Total"] = data["Cases"] + data["Deaths"]

with open(OUTPUT_FILE, 'w') as f:
    f.write("var table_data = ")
    f.write(str(data.values.tolist()))
    f.write(";")