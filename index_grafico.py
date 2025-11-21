from cotacao import get_cotacao
from grafico import *

opcao = 1

cotacoes = get_cotacao()

listNomeclaturas = ['JPY - Ienes','USD - Dólar', 'EUR - Euro', 'GBP - Libras']
listValores = [1 / cotacoes['JPY'], 1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]
print(listValores)

while opcao!=0:
    menu()
    opcao= int(input('Escolha um tipo de gráfico: '))

    match opcao:
        case 1:
            grafico_barras(listNomeclaturas, listValores)
        case 2:
            grafico_pizza(listNomeclaturas, listValores)
        case 3:
            grafico_dispersao(listNomeclaturas, listValores)