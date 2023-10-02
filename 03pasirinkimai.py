# suprogramuoti skaiciotuva veiksmai  + - * / ^-(kelimas laipsniu) ir &-(saknies traukimas)
import math
sk1 = int(input('sk1 = ...'))
veiksmas = input('pasirinkite veisma +, -, *, /, ^ (kelimas laipsniu) ir & (saknies traukimas)')
match veiksmas:
    case '+':
        sk2 = int(input('sk2 = ...'))
        suma = sk1 + sk2
        print( f'{sk1} + {sk2} = {suma}')

    case '-':
        sk2 = int(input('sk2 = ...'))
        suma = sk1 - sk2
        print( f'{sk1} - {sk2} = {suma}')
    
    case '*':
        sk2 = int(input('sk2 = ...'))
        suma = sk1 * sk2
        print( f'{sk1} * {sk2} = {suma}')


    case '/':
        sk2 = int(input('sk2 = ...'))
        suma = sk1 / sk2
        print( f'{sk1} / {sk2} = {suma}')

    case '^':
        laipsnis = int(input('laipsnis = ...'))
        suma = sk1**laipsnis
        print(f'{sk1}^{laipsnis}={suma}')
            
    case '&':
        saknis = int(input('saknis = ...'))
        suma = math.sqrt(math.pow(sk1,saknis))
        print(f'{sk1}&{saknis}={suma}')   

