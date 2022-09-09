import requests
from bs4 import BeautifulSoup

# OURO
def preco_ouro():
    requisicao_ouro = requests.get('https://goldrate.com/pt-br/grama-do-ouro-preco-cotacao-valor/').text
    sopa_ouro = BeautifulSoup(requisicao_ouro, 'html.parser')
    return sopa_ouro.select_one('.price-value').get_text()

# PETROLEO
def preco_pretroleo():
    requisicao_petroleo = requests.get('https://markets.businessinsider.com/commodities/oil-price?type=wti').text
    sopa_petroleo = BeautifulSoup(requisicao_petroleo, 'html.parser')
    return sopa_petroleo.select_one('div.price-section__values span').get_text()




