nome=str(input('Digite seu nome:'))
peso=int(input('Digite o seu peso:'))
altura=float(input('Digite sua altura em metros:'))
print()

print(nome, 'tem', altura, 'de altura, pesa', peso, 'kilos e seu IMC é de', f'{peso/altura**2:.2f}')
