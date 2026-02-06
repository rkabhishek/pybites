names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    i = 0

    for name, country in zip(names, countries):
        print(f'{i + 1}. {name:<11}{country}')
        i += 1
