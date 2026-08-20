COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
]
def value(colors):
    first_value = COLORS.index(colors[0])
    second_value = COLORS.index(colors[1])
    return int(f'{first_value}{second_value}')
