while True:
    num1=input('Digite o primeiro número: ')
    num2=input('Digite o segundo número: ')
    operador=input('Digite o operador: ')
    
    nums_validos=None
    num1_float=0
    num2_float=0
    
    try:
        num1_float=float(num1)
        num2_float=float(num2)
        nums_validos=True
    except:
        nums_validos=None
        
    if nums_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    if operador not in '+-*/':
        print('Operador inválido.')
        continue
    
    if len(operador)>1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando a conta: ')
    
    if operador=='+':
        print(num1_float+num2_float)
    elif operador=='-':
        print(num1_float-num2_float)
    elif operador=='*':
        print(num1_float*num2_float)
    elif operador=='/':
        print(num1_float/num2_float)
    
    sair=input('Deseja sair? (S/N): ').upper().startswith('S')
    
    if sair:
        break 