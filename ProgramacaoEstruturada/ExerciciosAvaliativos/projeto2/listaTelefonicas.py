# Wesley vitor silva de morais
# Criar um CRUD para um lista telefonica
#  Campos:
#     Nome
#     Email
#     Telefone
#     Data de Nascimento
#


def printaElementos(nomes,emails,telefones,data_nascimentos,profissoes):
  print("Nome ---- Email ---- Telefone ---- Data de Nascimento ---- Profissão")
  for valor in range(len(nomes)):
    print(nomes[valor], end=" ")
    print(emails[valor], end=" ")
    print(telefones[valor], end=" ")
    print(data_nascimentos[valor], end=" ")
    print(profissoes[valor], end=" ")
    print()
def printaElementoEspecifico(nomes,emails,telefones,data_nascimentos,profissoes):
  print()
  print("Nome:",nomes)
  print("Email:",emails)
  print("Telefone:",telefones)
  print("Data de Nascimento:",data_nascimentos)
  print("Profissão:",profissoes)

def verificaUsuario(emailUsuario,emails):
  return emailUsuario in emails

def atualizaCampo(lista, indice, novoValor):
  lista[indice] = novoValor

#Listas
nomes = []
emails = []
telefones = []
data_nascimentos = []
profissoes = []
opc = ''
menu = """  
###############################
##      Agenda Telefônica    ##
##      1 - Cadastrar        ##
##      2 - Pesquisar        ##
##      3 - Listar tudo      ##
##      4 - Apagar           ##
##      5 - Atualizar        ##
##      6 - Sair             ##
###############################
"""


while opc!='6':
  print(menu)
  opc = input("Digite sua opção:")

  if opc == '1':
    print()
    print("/modulo de cadastro")
    nome = input("Digite seu nome:")
    email = input("Digite seu email:")
    while email in emails:
      print("Email existente!!")
      print("Adicine outro email")
      email = input("Digite seu nome:")
    telefone = input("Digite seu telefone:")
    dataNascimento = input("Digite seu Data de nascimento:")
    profissao = input("Digite sua profissão:")

    nomes.append(nome)
    emails.append(email)
    telefones.append(telefone)
    data_nascimentos.append(dataNascimento)
    profissoes.append(profissao)

  elif opc == '2':
    print()
    print("/modulo de pesquisar")
    emailUsuario = input("Digite o email do usuário:")
    if verificaUsuario(emailUsuario,emails):
      indice = emails.index(emailUsuario)
      printaElementoEspecifico(nomes[indice],emails[indice],telefones[indice],data_nascimentos[indice],profissoes[indice])
    else:
      print("Usuário não encontrado!")
    
  elif opc =='3':
    print("/modulo de listar")
    printaElementos(nomes,emails,telefones,data_nascimentos,profissoes)

  elif opc == '4':
    print()
    print("/modulo de deletar")
    print("##############################")
    print("  1 - Deletar Todos            ")
    print("  2 - Deletar Específico       ")
    print("##############################")
    print()
    opcDeletar = input("Digite uma opção para deletar:")
    if opcDeletar == '1':
      nomes = []
      emails = []
      telefones = []
      data_nascimentos = []
      profissoes = []
    elif opcDeletar == '2':
      emailUsuario = input("Digite o email do usuário:")
      if verificaUsuario(emailUsuario,emails):
        indice = emails.index(emailUsuario)
        del nomes[indice]
        del emails[indice]
        del telefones[indice]
        del data_nascimentos[indice]
        del profissoes[indice]
      else:
        print("Usuário não existe!")
    else:
      print("Digite uma opção válida!")
    
  elif opc == '5':
    print()
    print("/modulo de Atualizar")
    emailUsuario = input("Digite o email do usuário:")
    if verificaUsuario(emailUsuario,emails):
      print("""   
        1 - Nome
        2 - Email
        3 - Telefone
        4 - Data de Nascimento
        5 - Profissão
      """)
      campo = input("Digite o campo a ser mudado:")
      valor = input("digite o novo valor do campo:")
      indice = emails.index(emailUsuario)

      if campo == '1':
        nomes[indice] = valor
      elif campo == '2':
        emails[indice] = valor
      elif campo == '3':
        telefones[indice] = valor
      elif campo == '4':
        data_nascimentos[indice] = valor
      elif campo == '5':
        profissoes[indice] = valor
    else:
      print("Usuário não encotrado!")
