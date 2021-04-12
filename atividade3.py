def exercicio1():
  num = int(input("Insira o numero: "))
  i=0
  while i <= num:
    if i % 5 == 0 and i % 2 != 0: 
     print(i)
    i+=1
exercicio1()

_____________________________________________

def exercicio2():
  num_entradas = int(input())
  lista = []
  i = 0
  while i < num_entradas:
    lista.append(input())
    i += 1
  return lista
retorno = exercicio2()
print(retorno)

______________________________________________

def exercicio3():
  num = input()
  lista = num.split()
  maior5 = []
  i = 0
  while i < len(lista):
    if int(lista[i]) > 5:
      maior5.append(int(lista[i]))
      i += 1
    else:
      i += 1
  return maior5
retorno = exercicio3()
print(retorno)

______________________________________________

def exercicio4():
  menu = {
  'a': 'PSG',
  'b': 'BAYERN',
  }
  opcao = input()
  while opcao != 'd':
    if opcao in menu:
      print(menu[opcao])  
    else:
      print("Invalido")
    opcao = input()          
exercicio4()
