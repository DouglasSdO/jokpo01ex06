##########################REFAZER######################

###BUG NA ENTRADA DE DADOS ERRO AO ENTRAR COM STRING


preco = input('Entre com o valor do produto:  ')
opcao = input('Escolha a forma de pagamento:\n 0 - '
'Á vista dinheiro:\n 1 - Á vista cartão:\n 2 - 2x no Cartão:\n 3 - 3x + Cartão ')
lista = ['Á vista dinheiro: ', 'Á vista cartão: ', '2x no Cartão', '3x + Cartão:']
print(lista[int(opcao)])

if preco.isnumeric() or opcao.isnumeric():
    vista_dinheiro = int(preco) * 10 /100
    print(f'O valor ficará em R$ {int(preco) - vista_dinheiro}')
elif opcao == 1:
    vista_cartao = int(preco) * 5 / 100
    print(f'O valor ficará em R$ {int(preco) - vista_cartao}')
elif opcao == 2:
    xx_cartao = preco
    print(f'O valor ficará em R$ {preco}')
elif opcao == 3:
    xxx_cartao = int(preco) * 20 / 100
    print(f'O valor ficará em R$ {int(preco) + xxx_cartao}')
else:
    print('Numero incorreto')



























#if escolha.isnumeric() and int(escolha) == 1:
        #numero = random.randint(1, 6)
        #print(f'{numero}')










#elif int(escolha) >= 2:
            #print('ok')
#elif:
    #print('numero incorreto, digite um numero valido')













#entrada = random.randint(1, 6)

#print(entrada)




