entrada = ''

while entrada != 'Ff' or entrada != 'Mm':
    entrada = str(input('Digite seu sexo: ')).strip().upper()
    if entrada != 'F' and entrada != 'M':
        print( 'Sexo invalido')
    if entrada == 'M':
        print('Sexo Masculino')
        break
    if entrada == 'F':
        print('Sexo feminino')
        break