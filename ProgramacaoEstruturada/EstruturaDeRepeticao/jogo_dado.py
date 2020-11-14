'''

Jogador quer jogar dados com o seu pc
Cada um tem seu dado de 6 faces 
Ele pode jogar quantas vezes quiser
No final diz o número de vitorias e empates

'''

import random

vUsario = 0
vPc = 0
empate = 0
sair = 0
while sair==0 or sair=='0':
  dadoUsuario = random.randint(1,6)
  dadoPc = random.randint(1,6)
  if dadoUsuario>dadoPc:
    print("Usuário ganhou!")
    vUsario+=1
  elif dadoPc > dadoUsuario:
    print("Pc ganhou!")
    vPc+=1
  else:
    print("Empate!")
    empate+=1
  print("Digite Algo diferente de 0 para sair!")
  sair = input("Selecione:")

print("-----------------")
print("Vitórias do Usuário:%d"%(vUsario))
print("Vitórias do Pc:%d"%(vPc))
print("Empate:%d"%(empate))


