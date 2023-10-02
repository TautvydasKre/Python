# For skirtas iteruojamiems dalykamas pvz sarasams
txt = 'Man rytais labai ž ŽŽ ąČą patinka anksti keltis ir eiti į mokyklą'
kiek = 0
lt = 'ąčęėįšųūĄČĘĖĮŠŲŪžŽ'
for i in txt:
    if i in lt:
        kiek +=1 # kiek = kiek +1
print(f'Sakinyje "{txt}" yra {kiek} lietuvišku simbolių')