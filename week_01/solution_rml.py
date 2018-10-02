from collections import defaultdict, Counter

visits = defaultdict(Counter)


def collect_places():
    visits.clear()  # empty out our vists

    while True:

        location = input("Tell me where you went: ").strip()

        if not location:
            break

        if location.count(',') != 1:
            print("That's not a legal city, country combination")
            continue

        city, country = location.split(',')

        visits[country.strip()][city.strip()] += 1


def display_places():
    for country, cities in sorted(visits.items()):
        print(country)
        for one_city, count in sorted(cities.items()):
            if count == 1:
                print(f"\t{one_city}")
            else:
                print(f"\t{one_city} ({count})")


if __name__ == '__main__':
    collect_places()
    display_places()