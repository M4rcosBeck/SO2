# coding: utf-8

import requests 
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
     
janela = Tk()
janela.title("Cotacao Atual de Moedas")
texto = Label(janela, text="Clique no botao para ver as cotacoes de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar Cotacoes", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()