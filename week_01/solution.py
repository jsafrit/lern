"""
I want you to create two different functions, collect_places and display_places.
Neither function takes an argument; instead, they will both work with a global variable, "visits".
"""
from collections import defaultdict, Counter


visits = defaultdict(list)


def collect_places():
    global visits
    visits.clear()
    while True:
        user_input = input('Tell me where you went: ')
        if user_input == '':
            break

        if ',' not in user_input:
            print("That's not a legal city, country combination")
            continue

        city, country = user_input.split(',', maxsplit=1)
        city = city.strip()
        country = country.strip()

        visits[country].append(city)

    # Now count duplicate visits and reformat the cities list
    count_cities()


def count_cities():
    global visits
    for country in sorted(visits):
        cities = sorted(visits[country])
        counter_cities = Counter(cities)
        new_cities = []
        for city, count in counter_cities.items():
            new_cities.append((city, count))
        visits[country] = new_cities


def display_places():
    for country in sorted(visits):
        print(country)
        cities = sorted(visits[country])

        for city, count in cities:
            if count > 1:
                print('    {} ({})'.format(city, count))
            else:
                print('    {}'.format(city))


if __name__ == '__main__':
    collect_places()
    display_places()
