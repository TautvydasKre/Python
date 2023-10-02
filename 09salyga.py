# ar blogas pazymis
# p = int(input('p = '))
# if p<=0 or p>=11:
#     print('Netinkamas')

def ivedimas():
    p = int(input('p = '))
    if not 1<=p<=10:
        print('Netinkamas. Kartokite ivedima')
        return ivedimas
    else:
        return p

paz = ivedimas()
print('pazymis',paz)