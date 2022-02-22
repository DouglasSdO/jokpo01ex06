"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é pár ou ímpar.
Caso o usuário não digite um numero inteiro informe que não é um numero inteiro.

"""

n1 = input('Digite um Numero Inteiro:  ')

if n1.isnumeric():
    par = int(n1) % 2
    if par == 0:
        print('====Numero Par====')
    else:
        print('====Numero Impar====')
else:
    print('====O numero não é inteiro====')

"""
Faça um programa que pergunte a hora do usuario e, baseando-se no horário descrito, exiba a saudação apropriada.
EX: 
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23

"""

hora = input('Digite seu horario: ')

if hora.isnumeric():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Digite um horario entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')

else:
    print('Digite um horario valido')

"""
Faça um programa que peça o primeiro nome do usuario. se o numero tiver 4 letras ou menos escreva
'seu nome é curto', se tiver entre 5 e 6 letras, escreva 
'seu nome é normal', maior que 6 letras escreva seu nome é muito grande;

"""
nome = str(input('Digite seu nome: '))

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) < 6 and len(nome) == 5:
    print('seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')










