## Jogo do PIM
##
## Gerar uma sequência de valores entre A e B
## (escolhidos pelo usuário), de forma que
## os múltiplos de 4 e valores terminados em 4
## sejam substituídos pela palavra PIM

## Ex: o jogador define o intervalo [10,20]
## O computador escreve:
## 10, 11, PIM, 13, PIM, 15, PIM, 17, 18, 19, PIM

valorInicial = int(input("Valor INicial:"))
valorFinal = int(input("Valor final:"))
lista = list(range(valorInicial,valorFinal))
for num in lista:
  if num%4==0 or str(num).split()[-1][-1]=='4':
    lista[lista.index(num)]='PIM'

print(lista)