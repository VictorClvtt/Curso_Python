
import os

palavra_secreta = 'victor'
letras_certas = ''
tentativas = 0

while True:
    
    palpite = input('Digite uma letra que você acha que está na palavra:')
    
    tentativas += 1
    
    if len(palpite) > 1:
        print('Digite uma letra por vez.')
        continue
        
    if palpite in palavra_secreta:
        letras_certas += palpite
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print(f'Palavra formada: {palavra_formada}')
            
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU PORRAAAAA!!!!!!')
        print(f'A palavra era {palavra_formada}')
        print(f'Tentativas: {tentativas}')
        letras_certas = ''
        tentativas = 0