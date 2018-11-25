#!/usr/bin/env python3

import requests
import csv

url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'

with open('cities.csv', 'w') as outfile:
    output = csv.writer(outfile, delimiter='\t')

    cities = [(d['city'], d['state'], d['rank'], d['population'])
              for d in requests.get(url).json()]

    output.writerows(cities)