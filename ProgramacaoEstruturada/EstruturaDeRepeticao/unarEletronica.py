'''
Escreva um programa em Python que simule uma eleição através de uma urna eletrônica.
O algoritmo deve ler um conjunto indeterminado de votos e computar os votos de cada
candidato, exibindo o resultado após o encerramento da votação.


'''

def existeNalista(lista, voto):
  for posicao in range(len(lista)+1):
    if voto in lista[posicao]:
      lista = computaOVoto(lista, posicao)
      break
  return lista

def computaOVoto(lista, candidato):
  lista[candidato][2] += 1
  return lista

def quemGanhou(lista):
  maiorVoto = lista[0][2]
  ganhador = lista[0][0]
  for nomeC, numC, votos in lista:
    if votos > maiorVoto:
      maiorVoto = votos
      ganhador = nomeC
  return ganhador

def candidatos():
  temMaisCandidadatos = 'S'
  lista = []
  while temMaisCandidadatos.upper()=='S':
    nomeCandidato = input("Digite o nome do candidato:")
    numeroCandidato = int(input("Digite o número do candidato:"))
    par = [nomeCandidato,numeroCandidato,0]
    lista.append(par)
    temMaisCandidadatos = input("Adicionar mais candidatos? S - N:")
  return lista


listaCandidatos = candidatos()

print("Sem os votos:",listaCandidatos)
querVotar = 'S'
while querVotar.upper()=='S':
  
  for nomeC, numC, vot in listaCandidatos:
    print("""
      Candidatos
      Nome: %s
      Número: %d
      -------------------------------
      """%(nomeC, numC))
  
  print("Digite o número do candidato:")
  voto = int(input("Número:"))
  listaCandidatos = existeNalista(listaCandidatos,voto)
  querVotar = input("Quer votar novamente? S -N")

print("Ganhador/Ganhadora:")
print(quemGanhou(listaCandidatos))

  
