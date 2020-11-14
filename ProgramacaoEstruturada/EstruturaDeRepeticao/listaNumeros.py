#Contador de 1 a 100
try:  
  valorInicial = int(input("Valor inicial:"))
  valorFinal = int(input("Valor Final:"))
  for num in range(valorInicial,valorFinal):
    print(num)
except ValueError:
  print("Adicione apenas valor inteiros")


