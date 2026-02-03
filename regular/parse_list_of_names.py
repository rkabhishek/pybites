import string
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    return [string.capwords(name) for name in set(names)]

def surname(name):
    return name.rsplit(maxsplit=1)[-1]

def len_first(name):
    return len(name.split(maxsplit=1)[0])

def sort_by_surname_desc(names):
    deduped_names = dedup_and_title_case_names(names)
    return sorted(deduped_names, key=surname, reverse=True)


def shortest_first_name(names):
    deduped_names = dedup_and_title_case_names(names)
    shortest_name = min(deduped_names, key=len_first)
    return shortest_name.split(maxsplit=1)[0]
