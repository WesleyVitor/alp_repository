qNotas = 4
somaNotas = 0
count = 1
sair = 0

while sair==0 or sair=='0':  

  try:
    while count<=qNotas:
      nota = float(input("Digite sua nota:"))
      somaNotas+=nota
      count+=1
    media = somaNotas/qNotas

    if media >= 7.0:
      print("Aprovado!")
    else:
      print("Reprovado")
  except:
    print("Deu ruim!")

  
  
  print("Se Quiser sair digite algo diferente de 0:")
  sair = input("Selecione:")
