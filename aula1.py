""""
* CRIAR VARIAVEIS PARA NOMES (STR), (IDADE), (INT).
* ALTURA (FLOAT) E PESO (FLOAT) DE UMA PESSOA.
* CRIAR VARIAVEIS COM O ANO ATUAL (INT).
* OBTER O ANO DE NASCIMENTO DA PESSOA BASEADO NA IDADE E NO ANO ATUAL.
* OBTER O IMC DA PESSOA COM 2 CASAS DECIMAIS (PESO E NA ALTURA DA PESSOA)
* EXIBIR UM TEXTO COM TODOS OS VALORES NA TELA USANDO F-STRINGS (COM CHAVES)
"""
nome = str(input('Digite seu nome: '))
alt = float(input('Altura: '))
peso = float(input('Peso: '))
ano = int(input('Digite o ano e nascimento: '))
imc = peso / alt**2

print(f'Seu nome é: {nome}.')
print(f'Sua altura é: {alt}m.')
print(f'Seu peso é: {peso}Kg.')
print(f'Sua idade é: {2022 - ano}.')
print(f'Seu imc é: 'f'{imc:.2f}.')


