import os

lista = []

print('Bem vindo ao seu programa de gerenciagento de lista de compras no terminal.')

while True:

    comando = input('O que deseja fazer? ([l]istar / [i]nserir / [a]pagar / [e]ncerrar): ').lower()

    while True:
        
        if comando == 'l':
            os.system('cls')
            if lista == []:
                comando = input('Sua lista se encontra vazia, deseja inserir elementos? ([s]im / [n]ão): ')
                
                if comando == 's':
                    comando = 'i'
                elif comando == 'n':
                    break
                else:
                    comando = input('Você digitou um comando inválido.')
                    break
            else:
                for nome in lista:
                    print(lista.index(nome), nome)
                break
   
        elif comando == 'i':
            os.system('cls')
            entrada = input('Digite o nome do elemento a ser adicionado: ')
                
            if not entrada.isdigit():
                lista.append(entrada)
            else:
                print('Tipo de dado não suportado.')
                
            comando = input('Adicionar outro elemento? ([s]im / [n]ão): ')
            os.system('cls')
            
            if comando == 's':
                comando = 'i'
                continue
            elif comando == 'n':
                break
            else:
                comando = input('Você digitou um comando inválido.')
                break
            
                
            
        elif comando == 'a':
            os.system('cls')
            if lista == []:
                comando = input('Sua lista se encontra vazia, deseja inserir elementos? ([s]im / [n]ão): ')
                if comando == 's':
                    comando = 'i'
                    continue
                elif comando == 'n':
                    break
                else:
                    comando = input('Você digitou um comando inválido.')
                    break
            else:
                for nome in lista:
                    print(lista.index(nome), nome)
                    
                try:   
                    lista.pop(int(input('Digite o índice do elemento que deseja apagar: ')))
                    print('ELEMENTO APAGADO.')
                except:
                    comando = input('Índice inválido, não foi possível apagar, deseja digitar outro? ([s]im / [n]ão): ')
                    if comando == 's':
                        comando = 'a'
                        continue
                    elif comando == 'n':
                        break
                    else:
                        comando = input('Você digitou um comando inválido.')
                        break
            
            comando = input('Deseja apagar mais algum elemento? ([s]im / [n]ão): ')
            os.system('cls')
            if comando == 's':
                comando = 'a'
                continue
            elif comando == 'n':
                break
            else:
                comando = input('Você digitou um comando inválido.')
                break
        elif comando == 'e':
            break
        else:
            print('Comando inválido.')
            break
    if comando == 'e':
        break