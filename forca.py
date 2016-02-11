# coding: utf-8

import os
from random import randrange
from ui import *

def joga():
    jogo_da_forca()

def jogo_da_forca():
    nome = da_boas_vindas()
    palavra = palavra_aleatoria()
    imprime_mascara(palavra)
    chutes = []
    erros = 0
    while erros < 5:
        chute = pede_chute()
        if len(chute) > 1:
            if chute == palavra:
                acertou_palavra(palavra)
                quit()
            else:
                errou_palavra(chute)
                erros = erros + 1
        else:
            chute_valido = valida_chute(chute, chutes)
            chutes.append(chute_valido)
            if acertou:
                mascara = palavra_mascarada(chutes, palavra)
            else:
                errou(chute_valido)
                erros = erros + 1
            print(mascara)

def obtem_arquivo():
    nome = ('palavras%s.txt' % (randrange(1, 4, 1)))
    arquivo = open(nome, 'r')
    conteudo = arquivo.read()
    palavras = conteudo.split('\n')
    arquivo.close()
    return palavras

def palavra_aleatoria():
    palavras = obtem_arquivo()
    palavra_escolhida = palavras[randrange(1, len(palavras), 1)]
    da_dica(palavras[0])
    return palavra_escolhida

def palavra_mascarada(chutes, palavra):
    mascara = ''
    for letra in palavra:
        for chute in chutes:
            indice = letra.find(chute)
            if indice != -1:
                mascara += letra
                break
        if indice == -1:
            mascara += '_'
    return mascara

def acertou(chute, palavra):
    if chute in list(palavra):
        return True
    else:
        return False

def valida_chute(chute, chutes):
    while chute in chutes:
        informa_chute_repetido(chute)
        chute = input()
    return chute

def errou(erros):
    avisa_que_errou(erro)
    erros += 1
    return erros