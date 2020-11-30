matriz = []

b1 = 10
b2 = 20
b3 = 30
b4 = 40
b5 = 60

for linha in range(4):
    matriz.append([b1,b2,b3,b4,b5])


for linha in range(4):
  for coluna in range(5):
    print("%d"%matriz[linha][coluna], end=" ")
  print("")

print()
for coluna in range(5):
  for linha in range(4):
    print("%d"%matriz[linha][coluna], end=" ")

  print("")
