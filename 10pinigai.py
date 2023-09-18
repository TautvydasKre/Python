# pradineSuma = int(input('Iveskite suma...'))
# eurai = pradineSuma // 100
# # centai = pradineSuma - (eurai * 100)
# centai = pradineSuma % 100
# print(f'{pradineSuma}cnt. = {eurai}eur. {centai}cnt.')

p = int(input('Iveskite prekiu skaiciu... '))
d = int(input('Kiek telpa i didele deze '))
m = int(input('Kiek telpa i maza deze '))
dkiek = p // d
likutis = p % d
mkiek = likutis // m
liko = likutis % m
print(f'reikes {dkiek} dideliu deziu, {mkiek} mazu deziu ir liks {liko} prekiu ')

