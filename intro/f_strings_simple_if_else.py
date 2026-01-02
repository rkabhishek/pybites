MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    is_allowed = 'is allowed' if age >= MIN_DRIVING_AGE else 'is not allowed'
    print(f'{name} {is_allowed} to drive')
