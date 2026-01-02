VALID_COLORS = ['blue', 'yellow', 'red']

def print_colors():
    while True:
        color = input().lower()
        if color == 'quit':
            print('bye')
            break
        elif color in VALID_COLORS:
            print(color)
        else:
            print('Not a valid color')
