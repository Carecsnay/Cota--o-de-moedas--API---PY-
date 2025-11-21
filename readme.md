# Conversor de Moedas

Este é um script em Python que funciona como um conversor de moedas via linha de comando. Ele utiliza a API pública [ExchangeRate-API](https://www.exchangerate-api.com/) para obter as taxas de câmbio mais recentes e realizar as conversões.

## Funcionalidades

-   Obtém taxas de câmbio em tempo real.
-   Converte valores entre diferentes moedas.
-   Menu interativo com opções pré-definidas (Dólar, Iene, Euro para Real).
-   Opção para escolher moedas de origem e destino personalizadas.

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

-   [Python 3.10](https://www.python.org/) ou superior (devido ao uso de `match/case`).
-   A biblioteca `requests` do Python.

## ⚙️ Instalação

1. Clone este repositório ou simplesmente baixe o arquivo `index.py`.

2. Instale a biblioteca `requests` usando o pip:
    ```bash
    pip install requests
    ```

## ▶️ Como Usar

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório onde você salvou o arquivo `index.py`.

3. Execute o script com o seguinte comando:

    ```bash
    python index.py
    ```

4. Um menu interativo será exibido:

    ```
    1 - Converter Dolar em Real
    2 - Converter Ienes em Real
    3 - Converter Euros em Real
    4 - Eu quero escolher
    0 - Sair!
    ```

5. Escolha uma das opções e siga as instruções na tela. Para a opção `4`, você precisará fornecer a sigla de 3 letras da moeda de origem e destino (ex: `USD`, `BRL`, `EUR`, `JPY`).
