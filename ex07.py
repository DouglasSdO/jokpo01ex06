'''prototipo longin de usuario'''

'''n = 0
s = 12345
while n != s:
    n = int(input('digite um numero: '))
    if n != s:
        print('Senha incorreta')
print('logado')'''

'''sexo = ''

while sexo != 'F' or sexo != 'M':
    sexo = str(input('Digite seu sexo: '))
    if sexo != 'F' and sexo != 'M':
        print('Sexo incorreto')
    if sexo == 'F':
        print('Voce é Femea')
        break
    if sexo == 'M':
        print('Voce é Macho')
        break'''






# sorteio de numeros

#FAZER COM QUE O PROGRAMA LEIA APENAS NUMEROS

'''import random

numero = 0
palp = 0
sorteio = random.randint(1, 10)

while sorteio != numero:
    numero = int(input('digite um numero:  '))
    if sorteio != numero:
        print(f'O numero não é {numero}!')
    palp += 1
    if palp >= 7:
        print('Tá dificil amigão?!')
if numero == sorteio:
    print(f'ACERTOU! O numero era {numero} e suas tentativas foram {palp}')'''





# Calculadora

'''n1 = int(input('Digite um numero:  '))
n2 = int(input('Digite outro numero:  '))
opcao = 0

while opcao != 5:
    if opcao > 5:
        print('Digite um numero valido')
    opcao = int(input(f'O que gostaria de fazer com {n1} e {n2}? '
    '\n=====Digite [1]===== Para somar. '
    '\n=====Digite [2]===== Para multiplicar. '
    '\n=====Digite [3]===== Para maior.'
    '\n=====Digite [4]===== Para novos numeros. '
    '\n=====Digite [5]===== Para sair. \n '))

    if opcao == 1:
        print(f'A soma dos valores {n1} e {n2} é {n1 + n2}')
    if opcao == 2:
        print(f'A multiplicação dos valores {n1} e {n2} é {n1 * n2}')
    if opcao == 3:
        if n1 > n2:
            print(f'O maior numero entre {n1} e {n2} é {n1}')
        if n2 > n1:
            print((f'O maior numero entre {n1} e {n2} é {n2}'))
    if opcao == 4:
        n1 = int(input('Digite um numero:  '))
        n2 = int(input('Digite outro numero:  '))
else:
    print('fim do pragrama.')'''

# progressao aritmetica

'''primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += razao
    cont += 1

print('End')'''


# sequencia de fibonacci

'''entrada = int(input('Digite um numero:  '))
t1 = 0
t2 = 1
cont = 3
print('{} {}'.format(t1, t2), end='')
while cont <= entrada:
    t3 = t1 + t2
    print(' {} '.format(t3), end= '')
    t1 = t2
    t2 = t3
    cont += 1'''

#n = 0
#cont = 0
#soma = 0
#while n != 999:
    #n = int(input('Digite um numero [999] para parar: '))
    #soma += n
    #cont += 1
#print(f'a soma foi {soma - 999} e foi digitados {cont - 1} numeros')

casa = int(input('Digite o valor da casa  R$:  '))
sal = int(input('Digite seu salario  R$:  '))
anos = int(input('Digite em quantos anos quer pagar:  '))

men = casa / (anos * 12)
sal1 = sal * 0.3

if men > sal1:
    print('Emprestimo negado sua mensalidade ficaria R$ {:.2f}'.format(men))
else:
    print('Emprestimo realizado com sucesso! mensalidade R$ {:2f}'.format(men))





















