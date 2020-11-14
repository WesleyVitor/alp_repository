#Múltiplos de um número
try:
  valorInicial = int(input("Valor Inicial:"))
  valorFinal = int(input("Valor Final:"))
  valorMultiplosEncontrar = int(input("Você quer saber os múltiplos de qual valor:"))
  if valorInicial<=valorFinal:
    step=1
  else:
    step=-1
  for num in range(valorInicial,valorFinal,step):
    if num%valorMultiplosEncontrar==0:
      print(num)
except ValueError:
  print("Adicione apenas valores inteiros")