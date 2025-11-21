import matplotlib.pyplot as plt

def grafico_barras(listNomeclaturas, listValores):
    plt.bar(listNomeclaturas, listValores)
    plt.title('Conversões para REAL (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('Valor em BRL')
    plt.show()

def grafico_pizza(listNomeclaturas, listValores):
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            absolute = round(float(pct/100.*total), 4)
            return f"{absolute} ({pct:.2f}%)"
        return my_format

    
    plt.pie(listValores, labels=listNomeclaturas, autopct=autopct_format(listValores))
    plt.title('Proporção em relação ao BRL (REAL) 1 para 1')
    plt.show()

def grafico_dispersao(listNomeclaturas, listValores):
    plt.scatter(listNomeclaturas, listValores)
    plt.title('Conversões para REAL (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('Valor em BRL')
    plt.show()

def menu():
    print()
    print('1 - Gráfico de Barras')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Sair')
    print()