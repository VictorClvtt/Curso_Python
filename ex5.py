'''
num = input('Digite um número inteiro: ')

if num.isdigit():
	
	num_int=int(num)
	
	if num_int%2==0:
		print(f'O número {num_int} é par.')
	elif num_int%2==1:
		print(f'O número {num_int} é ímpar.')
else:
	print(f'{num} não é um número inteiro.')
'''

'''
hora = input('Digite o hora atual: ')

try:
	
	hora = int(hora)
		
	if hora>=6 and hora<=12:
		print('Bom dia ^^')
	elif hora>12 and hora<=18:
		print('Boa tarde ;)')
	elif (hora>18 and hora<=24) or hora<6:
		print('Boa noite :D')
	else:
		print('Você digitou um horário inválido.')
except:
	print('Você não digitou um número inteiro.')
'''

'''
primeiro_nome = input('Digite o seu primeiro nome: ')

if len(primeiro_nome)<=4:
	print('Seu nome é curto.')
elif len(primeiro_nome)>4 and len(primeiro_nome)<=6:
	print('Seu nome é normal.')
else:
	print('Seu nome é muito grande.')
'''
