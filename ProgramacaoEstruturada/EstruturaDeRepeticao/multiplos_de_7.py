valorInicial = int(input("Valor inicial:"))
valorFinal = int(input("Valor final:"))
for num in range(valorInicial,valorFinal):
  if 7%num==0:
    print("Múltiplo:",num)