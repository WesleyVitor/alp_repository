#Lista valores impares entre 50 e 1

try:
  valorInicial = int(input("Valor Inicial:"))
  valorFinal = int(input("Valor Final:"))
  if valorInicial<=valorFinal:
    step = 1
  else:
    step = -1
  for num in range(valorInicial,valorFinal+step,step):
    if num%2==1:
      print(num)
except ValueError:
  print("Apenas valores inteiros")