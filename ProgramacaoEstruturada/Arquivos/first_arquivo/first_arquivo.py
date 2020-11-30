arquivo = open("texto.txt",'r')

# for linha in arquivo:
#   if not linha.startswith('All'):
#     continue
#   linha = linha.rstrip()
#   print(linha)

for linha in arquivo:
  if linha.find('revolution') == -1: continue
  linha = linha.rstrip()
  print(linha)