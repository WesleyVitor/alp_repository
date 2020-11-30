'''
1. Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela.
Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.
'''

numeros = []
soma = 0
for i in range(5):
  valor = float(input("Digite um valor:"))
  numeros.append(valor)
  soma +=valor

print()
print("Soma de Valores:",soma)
print("Valores digitados:")
for i in range(5):
  print(numeros[i])