from flask import Flask, render_template
from dados import commodities, data, moedas
from time import sleep

# GAMBIARRA DOS VALORES
dolar = moedas.dolar
euro = moedas.euro
yuan = moedas.yuan
dl_australiano = moedas.dolar_australiano
dl_sul = moedas.dolar_sul_africano

ouro = commodities.preco_ouro()
petroleo = commodities.preco_pretroleo()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/commodities")
def commodities():
    data_hora = data.DATA_HORA
    return render_template('commodities.html', dth=data_hora, ouro=ouro, petroleo=petroleo)


@app.route("/moedas")
def moedas():
    data_hora = data.DATA_HORA
    return render_template('moedas.html', dth=data_hora, dolar=dolar, euro=euro, yuan=yuan, dl_australiano=dl_australiano, dl_sul=dl_sul)


if __name__ == '__main__':
    app.run(debug=True)
