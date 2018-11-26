"""
This week, we're going to try to create some reports with Python's built-in data structures. For the purposes of this
exercise, I'm going to assume that we have a list of dictionaries, in which each dict represents a person. That dict
will then have three key-value pairs:

- name
- age
- hobbies

The final value, "hobbies", will be a list of strings describing the person's hobbies.

For example, here is a list of myself and my children:

    all_people = [{'name':'Reuven', 'age':48, 'hobbies':['Python', 'cooking', 'reading']},
                  {'name':'Atara', 'age':17, 'hobbies':['horses', 'cooking', 'art', 'reading']},
                  {'name':'Shikma', 'age':15, 'hobbies':['Python', 'piano', 'cooking', 'reading']},
                  {'name':'Amotz', 'age':13, 'hobbies':['biking', 'cooking']}]


You'll first want to create a list that looks like this. Note that we have a complex data structure here -- a list of
dicts, in which one of the dict's values is a list.

Given this data (or data like it), I'd like you to produce functions that produce a number of reports:

(1) Return the average age of all people, or (optionally) all people under a given age.
(2) Return a set of the different hobbies enjoyed by people in our database.
(3) Return a Counter object indicating how many people have each hobby -- that is, how many people are interested in
    Python, how many enjoy cooking, and so forth.  (I know, in an ideal world, everyone would love Python.  But hey,
    they're my children, so I'll forgive them.  For now.)
(4) Return the n most common hobbies, as a list of strings.

Hint: Nested list comprehensions and the Counter class will make this much easier!
"""
from collections import Counter


all_people = [{'name': 'Reuven', 'age': 48, 'hobbies': ['Python', 'cooking', 'reading']},
              {'name': 'Atara', 'age': 17, 'hobbies': ['horses', 'cooking', 'art', 'reading']},
              {'name': 'Shikma', 'age': 15, 'hobbies': ['Python', 'piano', 'cooking', 'reading']},
              {'name': 'Amotz', 'age': 13, 'hobbies': ['biking', 'cooking']}]


def average_age_under(people, maxage):
    if not people:
        return 0
    if maxage:
        all_age = [d['age'] for d in people if d['age'] < maxage]
    else:
        all_age = [d['age'] for d in people]
    if all_age:
        return sum(all_age)/len(all_age)
    else:
        return 0


def all_hobbies(people):
    hobbies = []
    for d in people:
        hobbies += d['hobbies']
    return set(hobbies)


def hobby_counter(people):
    if not people:
        return Counter()
    coll = [Counter(d['hobbies']) for d in people]
    all_counter = Counter()
    for c in coll:
        all_counter += c
    return all_counter


def n_most_common(people, param):
    n_counter = hobby_counter(people).most_common(param)
    top = [hobby for hobby, count in n_counter]
    return top


if __name__ == '__main__':
    print(average_age_under(all_people, None))
    print(all_hobbies(all_people))
    print(hobby_counter(all_people))
    print(n_most_common(all_people, 3))
