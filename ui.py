# coding: utf-8

def da_boas_vindas():
    print('\n\n')
    print('Bem vindo ao jogo da forca. Qual é o seu nome?')
    nome = input()
    print('\n')
    print('Seja bem vindo(a) %s. Vamos jogar!' % nome.capitalize())
    return nome

def imprime_mascara(palavra):
    mascara = ''
    for caractere in palavra:
        mascara = mascara + '_'
    print('A palavra contém %s caracteres' % (len(palavra)))

def pede_chute():
    print('\n')
    print('Entre com um chute ou a palavra inteira:')
    chute = input()
    while not chute:
        pede_chute()
    return chute

def avisa_que_errou(erro):
    print('\n')
    print('Desculpe, a letra %s não se encontra na palavra sorteada' % erro)

def da_dica(dica):
    print('\n')
    print('A dica da palavra chave é %s' % dica)

def acertou_palavra(palavra):
    print('\n')
    print('Parabéns, a palavra era %s' % palavra)

def errou_palavra(chute):
    print('\n')
    print('Desculpe, a palavra não é %s' % chute)

def informa_chute_repetido(chute):
    print('\n')
    print('O caractere %s já foi chutado, tente outro:' % chute)