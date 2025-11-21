from cotacao import converterCotacao

def menu():
    print()
    print('1 - Converter Dolar em Real')
    print('2 - Converter Ienes em Real')
    print('3 - Converter Euros em Real')
    print('4 - Eu quero escolher')
    print('0 - Sair!')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma opção: '))
    
    match opcao: 
        case 1:
            valor = input('Valor a ser convertido? ')
            valor = float(valor)
            print(converterCotacao('USD','BRL', valor))

        case 2:
            valor = input('Valor a ser convertido? ')
            valor = float(valor)
            print(converterCotacao('JPY','BRL', valor))

        case 3:
            valor = input('Valor a ser convertido? ')
            valor = float(valor)
            print(converterCotacao('EUR','BRL', valor))

        case 4:
            origem = str(input('Digite a nomeclatura da ORIGEM: '))
            destino = str(input('Digite a nomeclatura do DESTINO: '))
            valor = float(input('Digite o VALOR a ser comparado: '))

            resultado = converterCotacao(origem, destino, valor)
            print(resultado)

        case 0:
            exit