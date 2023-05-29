nome = 'João'
nome_diferente = ''

cont = 0
while cont < len(nome):
    nome_diferente += f'*{nome[cont]}'
    cont += 1

nome_diferente += '*'

print(nome_diferente)