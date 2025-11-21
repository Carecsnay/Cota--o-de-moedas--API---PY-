import matplotlib.pyplot as plt
from cotacao import get_cotacao

cotacoes = get_cotacao()

legNomeclaturas = ['JPY - Ienes','USD - Dólar', 'EUR - Euro', 'GBP - Libras']
legValores = [1 / cotacoes['JPY'], 1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]
print(legValores)

def grafico_barras(legNomeclaturas, legValores):
    plt.bar(legNomeclaturas, legValores)
    plt.title('Conversões para REAL (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('Valor em BRL')
    plt.show()

def grafico_pizza(legNomeclaturas, legValores):
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            absolute = round(float(pct/100.*total), 4)
            return f"{absolute} ({pct:.2f}%)"
        return my_format

    
    plt.pie(legValores, labels=legNomeclaturas, autopct=autopct_format(legValores))
    plt.title('Proporção em relação ao BRL (REAL) 1 para 1')
    plt.show()

def grafico_dispersao(legNomeclaturas, legValores):
    plt.scatter(legNomeclaturas, legValores)
    plt.title('Conversões para REAL (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('Valor em BRL')
    plt.show()

grafico_dispersao(legNomeclaturas, legValores)