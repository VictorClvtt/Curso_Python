nome=str(input('Digite seu nome:'))
sobrenome=str(input('Digite seu sobrenome:'))
ano_de_nascimento=int(input('Digite seu ano de nascimento:'))
idade=2023-ano_de_nascimento
altura=float(input('Digite sua altura em metros:'))
print()

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Ano de Nascimento:', ano_de_nascimento)
print('Idade:', idade)
print('É maior de idade?', idade>=18)
print('Altura em metros:', altura)
