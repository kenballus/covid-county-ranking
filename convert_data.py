# File: convert_data.py
# Author: Blake Wintermute
# Purpose: Converts the csv that comes out of scrape.py into a nested list for js

from pandas import read_csv

INPUT_FILE = "data.csv"
OUTPUT_FILE = "data.js"
data = read_csv(INPUT_FILE, names=["County", "State", "Population", "Cases", "Deaths", "Cases Per Capita", "Deaths Per Capita"]).fillna('')

with open(OUTPUT_FILE, 'w') as f:
    f.write("var table_data = ")
    f.write(str(data.values.tolist()))
    f.write(";")