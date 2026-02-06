names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    for i, (name, country) in enumerate(zip(names, countries), start=1):
        print(f'{i}. {name:<11}{country}')
