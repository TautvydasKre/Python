# ivedu savaites diena skaiciumi 1 man atspausdina pavadinima Pirmadienis

diena = int(input('Kokia savaites diena?'))
viskasOK = True
match diena:
    case 1:
        txt = 'pirmadienis'
    case 2:
        txt = 'antradienis'
    case 3:
        txt = 'treciadienis'
    case 4:
        txt = 'ketvirtadienis'
    case 5:
        txt = 'penktadienis'
    case 6:
        txt = 'sestadienis'
    case 7:
        txt = 'sekmadienis'
    case _:
        print('Blogai ivesti duomenys')
        viskasOK = False
if viskasOK :
    print (f'{diena} - {txt}')