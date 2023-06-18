x = int(input('Írj egy számot:'))
if x % 2 == 0:
    if x % 3 == 0:
        print('a szám osztható 2-vel és 3-mal')
    else:
        print('a szám osztható 2-vel, de 3-mal nem')
else:
    if x % 3 == 0:
        print('a szám osztható 3-mal, de 2-vel nem')
    else:
        print('a szám 2-vel nem, de 3-mal sem osztható')
