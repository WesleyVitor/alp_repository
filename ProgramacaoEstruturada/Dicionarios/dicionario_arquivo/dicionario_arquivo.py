file_name = input("Digite o nome do arquivo:")
try:
  arquivo = open(file_name)
except:
  print("Arquivo não existe!!")
  exit()

contador = dict()

for linha in arquivo:
  palavras = linha.split()
  for palavra in palavras:
    if not palavra in contador:
      contador[palavra] = 1
    else:
      contador[palavra] += 1

for chave in contador:
  print("%s - %d"%(chave, contador[chave]))