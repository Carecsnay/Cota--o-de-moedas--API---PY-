import requests

def get_cotacao(nomeclaturaDestino='BRL'):
    url = 'https://api.exchangerate-api.com/v4/latest/' + nomeclaturaDestino
    response = requests.get(url)
    data = response.json()

    if response.status_code==200:
        return data['rates']
    else:
        print('⚠️ Erro ao obter cotações!', response.status_code)
        return None
        
def converterCotacao(nomeclaturaOrigem, nomeclaturaDestino, valor): 
    rates = get_cotacao(nomeclaturaOrigem) 
    if rates:
        taxa_conversao = rates[nomeclaturaDestino]
        valor_convertido = round(valor * taxa_conversao, 4)
        return f'{valor} {nomeclaturaOrigem} equivale(m) a {valor_convertido} {nomeclaturaDestino}.'
    return 'Não foi possível obter a cotação.'

