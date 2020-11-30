"""
Wesley Vitor Silva de Morais
Eleição dos Eua 
Biden - 10
Trump - 11
"""
vBiden = 0
vTrump = 0
porcentagemBiden = 0
porcentagemTrump = 0
#Seção de votos
querVotar = 'S'
while querVotar.upper()=='S':
  print()
  print("Biden - 10")
  print("Trump - 11")
  try:
    voto = int(input("Digite o número do candidato que quer votar:"))
    if voto ==10:
      print("Você votou no Biden!")
      vBiden+=1
    elif voto==11:
      print("Você votou no Trump!")
      vTrump+=1
    else:
      print("Não existe candidato com esta numeração!")
  except ValueError:
    print("Digite apenas valores inteiros!")

  querVotar = input("Quer votar novamente? (s - n)")

#Contabilizar os votos
totalDeVotos = vBiden + vTrump
if totalDeVotos != 0:
  porcentagemBiden = vBiden / totalDeVotos * 100
  porcentagemTrump = vTrump / totalDeVotos * 100

if vBiden > vTrump:
  print()
  print("Biden é o novo Presidente!")
elif vTrump > vBiden:
  print()
  print("Trump é o novo Presidente!")
else:
  print()
  print("Ocorreu um empate nos votos!")
print()
print("Total de votos:")
print("Tivemos %d votos apurados"%(totalDeVotos))
print("Votos do Biden:%d voto(s)"%(vBiden))
print("Votos do Trump:%d voto(s)"%(vTrump))
print()
print("Porcentagem:")
print("Biden teve %.2f%% dos votos válidos"%(porcentagemBiden))
print("Trump teve %.2f%% dos votos válidos"%(porcentagemTrump))
print()




  