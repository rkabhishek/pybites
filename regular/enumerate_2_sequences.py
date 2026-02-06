names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    n = len(names)

    for i in range(n):
        print(f'{i + 1}. {names[i]:<11}{countries[i]}')
