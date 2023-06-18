import random

x = random.randint(1, 10)
y = int(input('Gondoltam egy számot, találd ki: '))
if x == y:
    print('Eltaláltad a számot.')
    print('Ügyes!')
    print('Gratulálok')
elif x - 1 == y or x + 1 == y:
    print('Ó, csak eggyel tévedtél!')
else:
    print('Sajnálom nem találtad el.')
    print('Hosszan gondolkodtálrajta!')
    print('Nem érte meg....')
    print('A szám a ', x, ' volt')
print('Viszlát')
