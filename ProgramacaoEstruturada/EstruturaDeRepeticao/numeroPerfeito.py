valorInicial = int(input("Valor Inicial:"))
valorFinal = int(input("Valor Final:"))
for n in range(valorInicial,valorFinal+1):
  count = 0
  soma = 0
  for i in range(1,n+1):
    if n%i==0:
      count+=1
      soma +=i
  if soma == n * 2:
    print()
    print("%d é um número perfeito!"%n)