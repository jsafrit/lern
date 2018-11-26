#!/usr/bin/env python3

from collections import Counter


def average_age_under(people, maxage=200):
    """Given a list of dicts, in which one of the keys is 'age', return the average age of all people.

If 'maxage' is passed, then only include those people younger than 'maxage' in the calculation."""

    young_ages = [one_person['age']
                  for one_person in people
                  if one_person['age'] < maxage]

    if young_ages:
        return sum(young_ages) / len(young_ages)
    else:
        return 0


def all_hobbies(people):
    """Given a list of dicts, in which one of the keys is 'hobbies' (a list of the person's hobbies), return a set of
    strings indicating which hobbies people have."""

    return {one_hobby
            for one_person in people
            for one_hobby in one_person['hobbies']}


def hobby_counter(people):
    """Given a list of dicts, in which one of the keys is 'hobbies' (a list of the person's hobbies), return a
    Counter object showing how many people have each hobby."""
    return Counter([one_hobby
                    for one_person in people
                    for one_hobby in one_person['hobbies']])


def n_most_common(people, n):
    """Given a list of dicts, in which one of the keys is 'hobbies' (a list of the person's hobbies), return a list
    of the n most common hobbies."""
    return [name
            for name, count in hobby_counter(people).most_common(n)]
