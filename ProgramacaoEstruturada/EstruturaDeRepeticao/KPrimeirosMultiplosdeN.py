primeirosMultiplos = int(input("Quantos primeiros multiplos você quer saber? :"))
valor = int(input("Você quer saber os multiplos de qual valor? :"))

for inteiro in range(1,primeirosMultiplos):
  multiplo = inteiro * valor
  print(multiplo)
