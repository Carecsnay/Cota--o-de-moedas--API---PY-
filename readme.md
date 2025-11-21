# Conversor de Moedas

Este é um projeto em Python que funciona como um conversor de moedas via linha de comando. Ele utiliza a API pública [ExchangeRate-API](https://www.exchangerate-api.com/) para obter as taxas de câmbio mais recentes e também permite a visualização de dados em gráficos.

## Funcionalidades

-   Obtém taxas de câmbio em tempo real.
-   Converte valores entre diferentes moedas.
-   Menu interativo com opções pré-definidas (Dólar, Iene, Euro para Real).
-   Opção para escolher moedas de origem e destino personalizadas.
-   Visualização da cotação de moedas (em relação ao Real) em diferentes tipos de gráficos (Barras, Pizza, Dispersão).

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

-   [Python 3.10](https://www.python.org/) ou superior (devido ao uso de `match/case`).
-   As bibliotecas `requests` e `matplotlib` do Python.

## ⚙️ Instalação

1. Clone este repositório ou baixe todos os arquivos `.py` para o mesmo diretório.

2. Instale as bibliotecas necessárias usando o pip:
    ```bash
    pip install requests
    pip install matplotlib
    ```

## ▶️ Como Usar

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório onde você salvou os arquivos do projeto.

3. Execute o script com o seguinte comando:

    ```bash
    python index.py
    ```

4. O menu principal será exibido:

    ```
    1 - Converter Dolar em Real
    2 - Converter Ienes em Real
    3 - Converter Euros em Real
    4 - Eu quero escolher
    5 - Eu quero ver os gráficos
    0 - Sair!
    ```

5. Escolha uma das opções e siga as instruções na tela.
    - Para a opção `4`, você precisará fornecer a sigla de 3 letras da moeda de origem e destino (ex: `USD`, `BRL`, `EUR`, `JPY`).
    - A opção `5` abrirá um novo menu para a seleção do tipo de gráfico que você deseja visualizar.

5. Imagens <br>
   ### Grafico de Pizza <br>
   <img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/68150437-0dab-4dde-94d9-7dd4052f96b5" /> <br>
   ### Grafico de Barras <br>
   <img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/857675a1-2e50-4a9b-9a00-ceb0d306048d" />



