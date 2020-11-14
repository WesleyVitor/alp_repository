valorInicial = int(input("Valor Inicial:"))
valorFinal = int(input("Valor Final:"))
if valorInicial>valorFinal:
  step = -1
else:
  step = 1

for valor in range(valorInicial,valorFinal+step,step):#Gerador de número no limite
  count = 0
  for inteiro in range(1, valor+1): #gerador de inteiro entre 1 e o numero
    if valor%inteiro==0: #verificador de divisor
      count +=1
  if count==2: #verificador de primo
    print(valor)
print()
