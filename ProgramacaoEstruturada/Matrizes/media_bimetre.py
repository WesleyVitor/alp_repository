matriz = []

b1 = 10
b2 = 20
b3 = 30
b4 = 40

for linha in range(4):
  for coluna in range(4):
    matriz.append([b1,b2,b3,b4])
  print("")


for linha in range(4):
  for coluna in range(4):
    print("%d"%matriz[linha][coluna], end=" ")
  print("")