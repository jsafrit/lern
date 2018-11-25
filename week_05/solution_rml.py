#!/usr/bin/env python3

import requests
import csv

gist_url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'


def cities_to_csv(url, filename):
    with open(filename, 'w', newline='') as outfile:
        output = csv.writer(outfile, delimiter='\t')

        cities = [(d['city'], d['state'], d['rank'], d['population'])
                  for d in requests.get(url).json()]

        output.writerows(cities)