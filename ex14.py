def multiplica_numero(numero, multiplicador):
    return numero*multiplicador

num = input('Digite o primeiro número: ')
multi = input('Digite o número multiplicador: ')

try:
    num = int(num)
    multi = int(multi)

    print(multiplica_numero(num, multi))
except:
    print('Valor não numérico digitado. ')