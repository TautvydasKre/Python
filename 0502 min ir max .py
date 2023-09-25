#ivedami du skaiciai. did priskirti didziausiam o maz maziausiaim
#nenaudoti min ir max funkciju
a = int(input('a=...'))
b = int(input('b=...'))

def isvedimas (did, maz):
    print (f'{did} daugiau uz {maz}')
    return did, maz


if a>b:
    isvedimas(a, b)
    print(f'{did} yra didesnis uz {maz}')
elif a<b:
    isvedimas(b, a)
else: 
    print(f'{a} lygus {b}')
