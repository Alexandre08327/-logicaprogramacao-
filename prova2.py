def exercicio1():
  nota1 = 5
  nota2 = 5
  nota3 = 5
  soma = nota1 + nota2 + nota3
  media = soma/3
  return 'Média do aluno é: ' + str(media)

______________________________________________

def exercicio2():
  tam_lista = int(input())
  lista = []
  i = 0
  while i < tam_lista:
    lista.append(input())
    i += 1
  return lista

_____________________________________________

def exercicio3():
  menu = {
  'a': 'globo',
  'b': 'sbt',
  }
  opcao = input()
  while opcao != 'z' and opcao != 'Z':
    if opcao in menu:
      print(menu[opcao])
    else:
      print("Invalido")
    opcao = input()
    
_____________________________________________
    
def exercicio4():
  lista = []
  menor7 = 0
  for i in lista:
    if i < 7:
      menor7 +=1
    if menor7/len(lista) >= 0.25:
     return("Professor Coxa")
  else:
     return("Professor Padrão")
