##Verifica o indice do elemento
def verifica_indice(array,elemento):
  isExist =  False
  cont = 0
  for i in array:
    if i==elemento:
      isExist = True
      break
  if not(isExist):
    raise ValueError("'%s' is not in list "%elemento)
  
  for j in array:
    if j == elemento:
      return print("Posição:",cont)
    cont +=1

print("Verifica o indice do elemtno")
lista = [1,2,3,4,"Maria","João","Felipe"]
valor = "JOse"
verifica_indice(lista,valor)
# print()
# print("Posição:",lista.index(valor))
