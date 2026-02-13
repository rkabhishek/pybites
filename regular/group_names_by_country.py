from collections import defaultdict

data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)

    info_list = data.strip().split("\n")[1:]
    for line in info_list:
        parts = line.split(",")
        if len(parts) != 3:
            raise ValueError("every line should have three parts separated by a comma")

        last_name, first_name, country = parts
        countries[country].append(f"{first_name} {last_name}")

    return countries
