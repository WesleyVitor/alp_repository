##Usando relação de recorrência
def fibo(n):
  if n==1 or n==0:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

numeroDeTermos = int(input("Digite o número de termos que você quer da sequência de fibonacci:"))
n=0
while n<=numeroDeTermos:
  print(fibo(n))
  n+=1
