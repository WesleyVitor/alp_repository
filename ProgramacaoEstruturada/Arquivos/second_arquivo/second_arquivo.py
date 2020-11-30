file_name = input("Digite o nome do arquivo:")
try:
  arquivo = open(file_name)
except:
  print("Arquivo não existe!!")
  exit()

for linha in arquivo:
  linha = linha.rstrip().upper()
  print(linha)