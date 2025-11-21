from cotacao import get_cotacao
from grafico import *

def _exibir_menu_grafico():
    print()
    print('1 - Gráfico de Barras')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Voltar ao menu principal')
    print()

def grafico_menu():
    cotacoes = get_cotacao()
    if not cotacoes:
        return

    listNomeclaturas = ['JPY - Ienes','USD - Dólar', 'EUR - Euro', 'GBP - Libras']
    listValores = [1 / cotacoes['JPY'], 1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]
    print(listValores)

    opcao = -1
    while opcao != 0:
        _exibir_menu_grafico()
        try:
            opcao = int(input('Escolha um tipo de gráfico: '))
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
            continue

        match opcao:
            case 1:
                grafico_barras(listNomeclaturas, listValores)
            case 2:
                grafico_pizza(listNomeclaturas, listValores)
            case 3:
                grafico_dispersao(listNomeclaturas, listValores)
            case 0:
                print("Voltando ao menu principal...")
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    grafico_menu()