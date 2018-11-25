"""
For this week's exercise, you are to download information in JSON format about the 1,000 largest cities. 
I've put it on GitHub as:

    https://gist.github.com/reuven/77edbb0292901f35019f17edb9794358

but you should download the "raw" version, which is here:

    https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json

After you retrieve the data and decode the JSON into Python data structures, I want you to create a CSV file. That 
file, which should have tabs as delimiters (rather than commas), should include the following data from the JSON file:
    City name
    State name
    City population
    City size rank
More specifically: You should write a function (cities_to_csv) that takes a URL and a filename. It'll download the 
JSON information from the URL, and then write it to the file specified.
"""
import csv
import requests
import json

gist_url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'


def cities_to_csv(gist_url, filename):
    r = requests.get(gist_url)
    data_json = r.content
    data = json.loads(data_json, encoding='utf-8')

    # fieldnames = data[0].keys()
    fieldnames = ['city', 'state', 'rank', 'population']

    with open(filename, 'w', newline='') as f:
        cw = csv.DictWriter(f, delimiter='\t', fieldnames=fieldnames, extrasaction='ignore')
        # cw.writeheader()
        for i in data:
            cw.writerow(i)

    return None

if __name__ == '__main__':
    cities_to_csv(gist_url, 'cities.csv')
