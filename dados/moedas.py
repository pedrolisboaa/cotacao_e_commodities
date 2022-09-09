import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,JPY-BRL,AUD-BRL,ZAR-BRL'
response = requests.get(url).json()

dolar = float(response['USDBRL']['bid'])
euro = float(response['EURBRL']['bid'])
yuan = float(response['JPYBRL']['bid'])
dolar_australiano = float(response['AUDBRL']['bid'])
dolar_sul_africano = float(response['ZARBRL']['bid'])

