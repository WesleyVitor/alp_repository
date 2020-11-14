import random
sair = 0
vUsuario = 0
vPc = 0
while sair==0 or sair =='0':
  print("C - coroa, K - cara")
  usuario = input("Escolha sua opção:")
  if usuario.upper == 'C':
    pc = 'K'
  else:
    pc = 'C'
  sorte = random.choice(['C','K'])
  if sorte == usuario:
    print("Vitória do Usuário")
    vUsuario+=1
  else:
    print("Vitória do PC")
    vPc +=1
  sair = input("Digite algo diferente de 0 para sair:")

print("------------------")
print("Vitórias::")
print("Vitórias do Usuário:%s"%(vUsuario))
print("Vitórias do Pc:%s"%(vPc))





