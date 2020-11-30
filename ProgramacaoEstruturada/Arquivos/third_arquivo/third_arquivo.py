
fname = open("arq.txt",'w')
texto = 'Texto contendo alguma coisa\n'
texto2 = 'Outro texto contendo alguma coisa'
fname.write(texto)
fname.write(texto2)
fname.close()
print("Lendo arquivo....")

fname = open("arq.txt")
for linha in fname:
  print(linha)
