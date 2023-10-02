# ivedu savaites diena skaiciumi patikrinti ar tai darbo diena ar savaitgalis

diena = int(input('Kokia savaites diena?'))
viskasOK = True
match diena:
    case 1 | 2 | 3 | 4| 5:
        txt = 'darbo diena'
    case 6 | 7:
        txt = 'savaitgalis'
    
    case _:
        print('Blogai ivesti duomenys')
        viskasOK = False
if viskasOK :
    print (f'{diena} - {txt}')