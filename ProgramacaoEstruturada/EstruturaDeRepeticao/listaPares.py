#Lista pares de 1 a 100

try:
  valorInicial = int(input("Valor Inicial:"))
  valorFinal = int(input("Valor Final:"))
  if valorInicial<=valorFinal:
    step = 1
  else:
    step = -1
  for num in range(valorInicial,valorFinal,step):
    if num%2==0:
      print(num)
except ValueError:
  print("Adicione apenas valores inteiros")