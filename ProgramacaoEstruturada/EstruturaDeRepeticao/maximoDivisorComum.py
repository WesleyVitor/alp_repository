def mdc(a,b):
  if b == 0:
    return a
  else:
    return mdc(b,a%b)

print("MDC entre dois valores")
a = int(input("Valor de A:"))
b = int(input("Valor de B:"))
#Algoritmo de euclides
print("MDC entre %d e %d:"%(a,b))
print(mdc(a,b))


