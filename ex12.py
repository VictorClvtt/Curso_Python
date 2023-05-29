novo_valor = 'n'
while True:    
    if novo_valor == 's':
        novo_valor = input('Deseja inserir outro CPF? ([s]im / [n]ão): ')
        if novo_valor == 's':
            cpf = input('Digite seu CPF: ')   
        else:
            break
    else:
        cpf = input('Digite seu CPF: ')
    
        if not int(cpf):
            cpf_sem_pontos = ''
            for numero in cpf:
                if numero.isdigit():
                    cpf_sem_pontos += numero
            cpf = cpf_sem_pontos
            del cpf_sem_pontos
    while True:
        if len(cpf) == 11:
            digitos = cpf[:9] 

            etapa = 0

            multiplicador = 10
            for digito in digitos:
                etapa += int(digito)*multiplicador
                multiplicador -= 1
                
            etapa *= 10
            etapa %= 11
            etapa = etapa if etapa<=9 else 0

            digitos += str(etapa)

            multiplicador = 11
            etapa = 0
            for digito in digitos:
                etapa += int(digito)*multiplicador
                multiplicador -= 1
                
            etapa *= 10
            etapa %= 11
            etapa = etapa if etapa<=9 else 0

            digitos += str(etapa)

            if digitos == cpf:
                print(f'O CPF {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} é válido!!!')
                novo_valor = 's'
                break
            else:
                print(f'O CPF {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]} não é válido!!!')
                novo_valor = 's'
                break
        else:
            print('Seu valor de entrada não corresponde ao formato esperado para verificação, digite novamente.')
            break