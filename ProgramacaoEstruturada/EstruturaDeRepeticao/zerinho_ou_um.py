'''
ZERINHO OU UM

#3 jogadores, sendo 1 humano e 2 computadores
#Será lançado os valores de 0 ou 1 de cada jogador
#Caso exista um jogador que colocou diferente de ambos, ele será o vencedor,
caso contrario terá um empate


'''

from random import randint

sair = 'N'
ptsJogadorHumano = 0
ptsJogadorPc1 = 0
ptsJogadorPc2 = 0
empates = 0
while sair.upper() == 'N':
  try:
    jogadorHumano = int(input("0 ou 1?"))
    if (jogadorHumano!=0) and (jogadorHumano!=1):
      print("Apenas 0 ou 1, espertinho!!")
      break
    jogadorPc1 = randint(0,1)
    jogadorPc2 = randint(0,1)
    
    if (jogadorHumano != jogadorPc1) and (jogadorHumano!=jogadorPc2):
      print("Jogador Humano ganhou!")
      ptsJogadorHumano+=1
    elif (jogadorPc1!=jogadorHumano) and (jogadorPc1!=jogadorPc2):
      print("Jogador Computador 1 ganhou!")
      ptsJogadorPc1+=1
    elif (jogadorPc2!=jogadorHumano) and (jogadorPc2!=jogadorPc1):
      print("Jogador Computador 2 ganhou!")
      ptsJogadorPc2+=1
    elif (jogadorHumano==jogadorPc1) and (jogadorHumano==jogadorPc2):
      print("Empate")
      empates+=1
    sair = input("Quer sair ? S - Sim , N -Não:")
  except:
    print("Coloque valores inteiros!!")


print("Pontuação")
print("Pontos jogador humano:",ptsJogadorHumano)
print("Pontos jogador Computador 1:",ptsJogadorPc1)
print("Pontos jogador Computador 2:",ptsJogadorPc2)
print("Empates:",empates)





    
  