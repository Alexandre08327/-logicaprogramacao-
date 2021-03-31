def calcula_soma(lista):
  lista = [2,4,6]
  soma = 0
  for num in lista:
    soma += num
  return soma

retorno = calcula_soma([])
print(retorno)

______________________________________________________

def converte_entrada(texto):
  texto = str(input())
  lista = texto.split()
  return lista

retorno = converte_entrada('texto')  
print(retorno)

______________________________________________________

def processa_numeros(lista):
  lista = []
  soma = 0
  elementos = len(lista)
  for num in lista:
    soma += num 
  return (soma, elementos)
  
retorno = processa_numeros([])
print(retorno)

_______________________________________________________

def main():
  entrada = input() 
  lista = entrada.split()
  soma = 0 
  for num in lista:
    soma += int(num)
  media = soma/len(lista)
  return media

retorno = main()
print(retorno)
