def uncommon_cities(my_cities, other_cities):
    uncommon = []

    for city in my_cities:
        if city not in other_cities:
            uncommon.append(city)


    for city in other_cities:
        if city not in my_cities:
            uncommon.append(city)

    return len(uncommon)
