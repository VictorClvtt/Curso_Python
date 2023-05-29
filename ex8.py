frase = 'Python é uma linguagem de programação multiparadígma.'


letra_mais_frequente = ''
frequencia_maior = 0
i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_aparece = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if frequencia_maior < quantas_vezes_aparece:
        frequencia_maior = quantas_vezes_aparece
        letra_mais_frequente = letra_atual
    
    print(quantas_vezes_aparece, letra_atual)
    
    i += 1
    
print(f'A letra mais frequente foi "{letra_mais_frequente}", e ela apareceu {frequencia_maior} vezes')