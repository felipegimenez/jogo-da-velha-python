# encoding: utf-8
tabuleiro = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}

nomejogador1 = raw_input('Qual o seu nome, jogador X? ')
nomejogador2 = raw_input('Qual o seu nome, jogador O? ')
mensagem_vitoria = 'Valeu, {}...Você ganhou do {}...ele é muito ruim'

def imprimeTabuleiro():
    print('Jogo da Velha bem legal!')
    print(tabuleiro[1] + '|' + tabuleiro[2] + '|' + tabuleiro[3])
    print('-+-+-')
    print(tabuleiro[4] + '|' + tabuleiro[5] + '|' + tabuleiro[6])
    print('-+-+-')
    print(tabuleiro[7] + '|' + tabuleiro[8] + '|' + tabuleiro[9])

imprimeTabuleiro()

def jogar():
    jogadas = 0
    jogadorAtual = 'X'

    while True:
        if jogadas == 9:
                print('Vixiiiiii! Deu velha.')
                break

        if jogadorAtual == 'X':
            jogada = entradaDeDados('X', nomejogador1)
        else:
            jogada = entradaDeDados('O', nomejogador2)

        if jogada < 1 or jogada > 9:
            print 'Jogue entre 1 e 9'
            imprimeTabuleiro()
            continue

        if tabuleiro[jogada] == 'X' or tabuleiro[jogada] == 'O':
            print 'Posicão já preenchida'
            imprimeTabuleiro()
            continue

        tabuleiro[jogada] = jogadorAtual

        if verificarGanhador(jogador='X'):
            print mensagem_vitoria.format(nomejogador1, nomejogador2)
            imprimeTabuleiro()
            break
        if verificarGanhador(jogador='O'):
            print mensagem_vitoria.format(nomejogador2, nomejogador1)
            imprimeTabuleiro()
            break


        jogadorAtual = 'X' if jogadorAtual == 'O' else 'O'
        jogadas +=1

        imprimeTabuleiro()

def entradaDeDados(jogadorAtual, nomeJogador ):
    while True:
        try:
            jogada = int(raw_input('Qual a sua jogada, {}? ({}) '.format(nomeJogador, jogadorAtual)))
            return jogada
        except ValueError:
            print 'Digite um número! (de 1 a 9)'
            imprimeTabuleiro()

def verificarGanhador(jogador):
    if (tabuleiro[1] == jogador and tabuleiro[2] == jogador and tabuleiro[3] == jogador):
        return True
    elif (tabuleiro[4] == jogador and tabuleiro[5] == jogador and tabuleiro[6] == jogador):
        return True
    elif (tabuleiro[7] == jogador and tabuleiro[8] == jogador and tabuleiro[9] == jogador):
        return True
    elif (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador):
        return True
    elif (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador):
        return True
    elif (tabuleiro[3] == jogador and tabuleiro[6] == jogador and tabuleiro[9] == jogador):
        return True
    elif (tabuleiro[1] == jogador and tabuleiro[5] == jogador and tabuleiro[9] == jogador):
        return True
    elif (tabuleiro[3] == jogador and tabuleiro[5] == jogador and tabuleiro[7] == jogador):
        return True

jogar()
