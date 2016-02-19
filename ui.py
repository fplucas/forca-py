# coding: utf-8

def da_boas_vindas():
    print('\n\n')
    print('Bem vindo ao jogo da forca. Qual é o seu nome?')
    nome = input().capitalize()
    print('\n')
    print('Seja bem vindo(a) %s. Vamos jogar!' % nome)
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
        chute = pede_chute()
    return chute

def jogar_novamente():
    print('Deseja jogar novamente? (S/N)')
    resposta = input().upper()
    if resposta == 'S':
        resposta = True
    else:
        resposta = False
    return resposta

def avisa_que_errou(erro):
    print('\n')
    print('Desculpe, a letra %s não se encontra na palavra sorteada' % erro)

def da_dica(dica):
    print('\n')
    print('A dica da palavra chave é %s' % dica)

def acertou_palavra(palavra):
    print('\n')
    print('Parabéns, a palavra era %s' % palavra)

def avisa_que_errou_palavra(palavra):
    print('\n')
    print('Desculpe, a palavra não é %s' % palavra)

def informa_chute_repetido(chute):
    print('\n')
    print('O caractere %s já foi chutado, tente outro:' % chute)

def informa_que_perdeu(nome):
    print('\n\n')
    print('Desculpe %s, não foi dessa vez, tente novamente' % nome)