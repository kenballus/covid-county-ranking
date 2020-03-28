# File: scrape.py
# Author: Ben Kallus
# Purpose: Grabs the latest COVID-19 data from nytimes.com and formats it into a csv

from selenium import webdriver
from pandas import read_csv


STATES = ["Alabama", "American Samoa", "Northern Mariana Islands", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Virgin Islands", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
INPUT_FILE = "data.csv"
OUTPUT_FILE = "data.js"


class DataNode:
    """ Stores COVID-19 data for one region. """
    def __init__(self):
        self.state = ""
        self.county = ""
        self.cases = 0
        self.deaths = 0
        self.population = 0
        self.cases_per_thousand = 0.0
        self.deaths_per_thousand = 0.0
        self.death_rate = 0.0

    def __str__(self):
        return ",".join([self.county, self.state, str(self.population), str(self.cases), str(self.deaths), str(self.cases_per_thousand), str(self.deaths_per_thousand), str(self.death_rate)])


def main():
    browser = webdriver.Firefox()
    browser.get("https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html?action=click&module=Spotlight&pgtype=Homepage#g-cases-by-county")

    # Find the div with id g-cases-by-county
    candidates = browser.find_element_by_id("g-cases-by-county").find_elements_by_class_name("svelte-ffcf53")

    # Find the table and the button
    button = None
    table = None
    for candidate in candidates:
        if candidate.tag_name == "button":
            button = candidate
        elif candidate.tag_name == "table":
            table = candidate

        if button is not None and table is not None:
            break

    # Click the button
    button.click()


    # Grab the data table
    lines = table.text.split("\n")[1:]
    browser.quit() # Done with this now

    # Grab the census population data
    populations = {}

    for line in open("populations.csv", "r").readlines():
        trio = line.split(",")
        if trio[1] not in populations:
            populations[trio[1]] = {}

        populations[trio[1]][trio[0]] = trio[2]

    # Extract the data from the table
    nodes = []
    for line in lines:
        orig = line
        node = DataNode()
        for state in STATES:
            if line.startswith(state):
                node.state = state
                line = line[len(state) + 1:]
                break

        if not line[0].isdigit(): # If we have a county
            for c_idx in range(len(line)):
                if line[c_idx].isdigit():
                    node.county = line[:c_idx - 1]
                    line = line[c_idx:]
                    break

        # The unknown counties are not relevant to our data set
        if node.county == "Unknown":
            continue
        if node.county == "":
            node.county = node.state

        line = line.replace(",", "") # Get rid of ,s in the numbers
        node.cases = int(line.split(" ")[0])
        node.deaths = int(line.split(" ")[1])
        node.death_rate = node.deaths / node.cases

        node.population = int(populations[node.state][node.county])
        node.cases_per_thousand = node.cases / node.population * 1000
        node.deaths_per_thousand = node.deaths / node.population * 1000

        nodes.append(node)


    nodes = sorted(nodes, key=lambda node: node.cases, reverse=True)

    # Write the csv
    open("data.csv", "w+").write("\n".join([str(node) for node in nodes]))

    # Create the js data file
    data = read_csv(INPUT_FILE, names=["County", "State", "Population", "Cases", "Deaths", "Cases Per Thousand", "Deaths Per Thousand", "Death Rate"]).fillna("")
    with open(OUTPUT_FILE, "w") as f:
        f.write("var table_data = ")
        f.write(str(data.values.tolist()))
        f.write(";")


if __name__ == "__main__":
    main()