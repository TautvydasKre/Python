#ivedami du skaiciai. did priskirti didziausiam o maz maziausiaim
#nenaudoti min ir max funkciju
a = int(input('a=...'))
b = int(input('b=...'))

if a>b:
    did = a
    maz = b
    print(f'{did} yra didesnis uz {maz}')
elif b>a:
    did = b
    maz = a
    print(f'{did} yra didesnis uz {maz}')
else:
    print(f'{a} lyus {b}')
