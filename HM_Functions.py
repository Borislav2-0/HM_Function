def print_params(aircraft=5, ships=True, tanks='string'):
    print(aircraft, ships, tanks)


print_params()
print_params(aircraft=15, tanks='text')
print_params(ships=False, tanks=['text', 'string', 'word'])

print()
mil_technics = ['aircraft', 'ships', 'tanks']
dict_ = {'aircraft': 'IL-2', 'tank': 'PT-76B', 'ship': 'Novik'}
print_params(*mil_technics)
mil_technics_2 = ['BTR-80', 'SU-25']
print_params(*mil_technics_2, False)
print_params(**{'aircraft': 'IL-2','ships': 'Novik', 'tanks': 'PT-76B'})
