'''

JOGO DO 7 OU 11

#2 dados serão jogados pelo jogador1
#se a soma dos dados derem 7 ou 11 ponto ao jogador,caso contrario ponto do pc


'''
from random import randint


ptsJogador = 0
ptsPc = 0
sair = 'N'
while sair.upper() =='N':
  dado1 = randint(1,6)
  print("Dado 1:",dado1)
  dado2 = randint(1,6)
  print("Dado 2:",dado2)
  soma = dado1 + dado2
  if (soma == 7) or (soma == 11):
    ptsJogador+=1
  else:
    ptsPc+=1
  sair = input("Deseja sair? S - Sim ou N - Não:")

print("Pontuação")
print("Pontos do jogador:",ptsJogador)
print("-----------------------------")
print("Pontos do computador:",ptsPc)
