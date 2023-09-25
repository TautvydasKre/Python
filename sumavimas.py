# parasyti programa, kuri sudeda du skaicius (su  funkcijomis)
#
def ivedimas (txt):
    sk = int(input(f'{txt}=...'))
    return sk

def sumavimas():
    sk1 = ivedimas('Pirmas')
    sk2 = ivedimas('Antras')
    suma = sk1 + sk2
    return suma , sk1 , sk2

def rezultatas():
    
    suma , a, b = sumavimas()
    print(f'{a}+{b}={suma}')

rezultatas()
