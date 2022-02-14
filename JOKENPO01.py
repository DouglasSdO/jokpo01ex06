###################REFAZER################

###BUG NA ENTRADA DE DADOS ERRO AO ENTRAR COM STRING


from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# Jogador faz a escolha

print('''Suas opções:
 [0] Pedra
 [1] Papel
 [2] Tesoura  ''')

jogador =int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('=='*11)

print(f'O computador jogou:{itens[computador]}')
print(f'O jogador jogou: {itens[jogador]}')

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Voce Venceu!!!')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Opção Invalida')

elif computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 0:
        print('Computador venceu')
    elif jogador == 2:
        print('Voce Venceu!!!')
    else:
        print('Opção Invalida')

elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('Voce Venceu!!!')
    elif jogador == 1:
        print('Computador Venceu')
    else:
        print('Opção Invalida')







