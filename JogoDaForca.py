#Desafio: Jogo da Forca
import random

palavras = ['NINTENDO', 'CONTROLE', 'JOGOS', 'POKEMON', 'GENGAR', 'PIKACHU', 'PSYDUCK', 'SNORLAX', 'BULBASAUR', 'MUDKIP']

palavraSecreta = palavras[random.randint(0, 9)]
tracinhos = ['_'] * len(palavraSecreta)
tentativas = len(palavraSecreta) + 4
contador = tentativas
acertos = 0


nintendo = ['N', 'I', 'N', 'T', 'E', 'N', 'D', 'O']
controle = ['C', 'O', 'N', 'T', 'R', 'O', 'L', 'E']
jogos = ['J', 'O', 'G', 'O', 'S']
pokemon = ['P', 'O', 'K', 'E', 'M', 'O', 'N']
gengar = ['G', 'E', 'N', 'G', 'A', 'R']
pikachu = ['P', 'I', 'K', 'A', 'C', 'H', 'U']
psyduck = ['P', 'S', 'Y', 'D', 'U', 'C', 'K']
snorlax = ['S', 'N', 'O', 'R', 'L', 'A', 'X']
bulbasaur = ['B', 'U', 'L', 'B', 'A', 'S', 'A', 'U', 'R']
mudkip = ['M', 'U', 'D', 'K', 'I', 'P']

for i in range(0, tentativas):
    print('----------------------------------------------')
    print('tente uma letra para acertar a palavra\n')
    contador -= 1
    print(f'você tem {contador} tentativas restantes\n')
    print(f'você tem {acertos} acertos\n')
    print(*tracinhos)

    resposta = input("Digite uma letra:\n").capitalize()
    if palavraSecreta == "NINTENDO":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 8):
                if resposta == nintendo[j]:
                    tracinhos[j] = nintendo[j]
                    acertos += 1
    elif palavraSecreta == "CONTROLE":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 8):
                if resposta == controle[j]:
                    tracinhos[j] = controle[j]
                    acertos += 1
    elif palavraSecreta == "JOGOS":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 5):
                if resposta == jogos[j]:
                    tracinhos[j] = jogos[j]
                    acertos += 1
    elif palavraSecreta == "POKEMON":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 7):
                if resposta == pokemon[j]:
                    tracinhos[j] = pokemon[j]
                    acertos += 1
    elif palavraSecreta == "GENGAR":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 6):
                if resposta == gengar[j]:
                    tracinhos[j] = gengar[j]
                    acertos += 1
    elif palavraSecreta == "PIKACHU":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 7):
                if resposta == pikachu[j]:
                    tracinhos[j] = pikachu[j]
                    acertos += 1
    elif palavraSecreta == "PSYDUCK":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 7):
                if resposta == psyduck[j]:
                    tracinhos[j] = psyduck[j]
                    acertos += 1
    elif palavraSecreta == "SNORLAX":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 7):
                if resposta == snorlax[j]:
                    tracinhos[j] = snorlax[j]
                    acertos += 1
    elif palavraSecreta == "BULBASAUR":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 9):
                if resposta == bulbasaur[j]:
                    tracinhos[j] = bulbasaur[j]
                    acertos += 1
    elif palavraSecreta == "MUDKIP":
        if len(resposta) > 1:
            print('-resposta invalida-\n')
        else:
            for j in range(0, 6):
                if resposta == mudkip[j]:
                    tracinhos[j] = mudkip[j]
                    acertos += 1
    if tracinhos == nintendo or tracinhos == controle or tracinhos == jogos or tracinhos == pokemon or tracinhos == gengar or tracinhos == pikachu or tracinhos == psyduck or tracinhos == snorlax or tracinhos == bulbasaur or tracinhos ==mudkip:
        print('você acertou tudo, parabens!!!!')
        print('--------------------------------------------')
        break
if tracinhos != nintendo and tracinhos != controle and tracinhos != jogos and tracinhos != pokemon and tracinhos != gengar and tracinhos != pikachu and tracinhos != psyduck and tracinhos != snorlax and tracinhos != bulbasaur and tracinhos != mudkip:
    print('você perdeu, que pena')
    print('--------------------------------------------')











