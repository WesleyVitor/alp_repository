def mdc(a,b):
  while b!=0:
    r = a%b
    a=b
    b=r
  return a
a = int(input("Valor de A:"))
b = int(input("Valor de B:"))
mmc = (a*b)/mdc(a,b)
print("MMC entre %d e %d:"%(a,b))

print(mmc)