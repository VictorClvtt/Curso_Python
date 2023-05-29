perguntas = [
    {
        '1' : 'Qual é a raíz quadrada de 4?',
        'Opções' : ['3', '11', '20', '2'],
        'Resposta' : '2'
    },
    {
        '2' : '41 + 67432 é igual a quanto?',
        'Opções' : ['3', '67473', '20', '2'],
        'Resposta' : '67473'
    }
]

i = 1
acertos = 0
for pergunta in perguntas:
    print(f'Pergunta {i}: {pergunta[str(i)]}')
    for i2, opcao in enumerate(pergunta['Opções']):
        print(f'{i2}: {opcao}')
    
    resposta = input('Escolha uma opção: ')

    resposta_int = None

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < len(pergunta['Opções']):
            if pergunta['Opções'][resposta_int] == pergunta['Resposta']:
                acertos += 1
                print('Acertou 👌')
            else:
                print('Errou 👎')

    i += 1

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')