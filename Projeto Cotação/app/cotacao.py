# coding: utf-8

import requests 

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    print(f"Dolar: {cotacao_dolar}\nEuro: {cotacao_euro}\nBitCoin: {cotacao_btc}")

pegar_cotacoes()