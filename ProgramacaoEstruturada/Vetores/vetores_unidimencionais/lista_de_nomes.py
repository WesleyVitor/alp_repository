'''
2. Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou, um por linha.
'''

nomes = []
vI = 0
while vI < 5:
  nome = input("Digite um nome:")
  nomes.append(nome)
  vI +=1
print()
print("Valores digitados:")
vI -=1
while vI >= 0:
  print("Valor:",nomes[vI])
  vI -=1