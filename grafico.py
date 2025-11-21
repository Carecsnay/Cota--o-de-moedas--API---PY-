import matplotlib.pyplot as plt
from cotacao import get_cotacao

cotacoes = get_cotacao()

legNomeclaturas = ['JPY - Ienes','USD - Dólar', 'EUR - Euro', 'GBP - Libras']
legValores = [1 / cotacoes['JPY'], 1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]
print(legValores)

plt.bar(legNomeclaturas, legValores)
plt.title('Conversões para REAL (BRL)')
plt.xlabel('Moedas')
plt.ylabel('Valor em BRL')
plt.show()