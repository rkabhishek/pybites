from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType) -> str:
    return ", ".join(cars['Jeep'])

def get_first_model_each_manufacturer(cars: CarsType) -> List[str]:
    return [models[0] for models in cars.values()]

def get_all_matching_models(cars: CarsType, grep: str = DEFAULT_SEARCH) -> List[str]:
    g = grep.lower()
    return sorted(car for models in cars.values() for car in models if g in car.lower())

def sort_car_models(cars: CarsType) -> CarsType:
    return {k: sorted(v) for k, v in cars.items()}
