''' Você foi requisitado a elaborar um algoritmo para
identificar as cem pessoas mais influentes da rede, a fim de engajá-las numa campanha
publicitária. A agência dispõe de um arquivo cujos registros incluem o nome da pessoa
e a quantidade de amigos que ela possui na rede. A pessoa x é mais influente que a
pessoa y se o número de amigos de x for maior que o número de amigos de y, na rede
social. Você pode supor que os dados do arquivo cabem em memória primária. Se duas
ou mais pessoas forem igualmente influentes, você pode escolher arbitrariamente entre
elas quando estiver coletando os últimos dados. '''
import collections
import random
import math

def merge(V,left,middle,right):
    
  L = []
  R = []
  
  for i in range(left,middle+1):
    L.append(V[i])

  for j in range(middle+1,right+1):
    R.append(V[j])
    
  i = j = 0
  k = left

  while i < len(L) and j < len(R):
    if L[i].friends >= R[j].friends:
      V[k] = L[i]
      i += 1
      k += 1
    else:
      V[k] = R[j]
      j += 1
      k += 1

  while i < len(L):
    V[k] = L[i]
    i += 1
    k += 1
  
  while j < len(R):
    V[k] = R[j]
    j += 1
    k += 1
  
def mergeSort(V,left,right):
  if left < right:
    middle = math.floor((left+right)/2)
    mergeSort(V,left,middle)
    mergeSort(V,middle+1,right)
    merge(V,left,middle,right)

if __name__ == "__main__":

    User = collections.namedtuple('User', ['name', 'friends'])
    # Quantidade de usuarios da rede social
    n = 10
    # Gerando lista com os dados dos usuarios
    users = [[] for i in range(n)]

    # Gerando aleatoriamente nome e quantidade
    # de amigos para os usuarios
    for i in range(n):
        # Considerando que o usuario tem, no minimo, um amigo
        r = random.randint(1, i+1)
        name = 'Name' + str(i)
        friends = r
        users[i] = User(name, friends)

    # Imprimindo todos os usuarios da rede social
    for i in range(n):
        print(f'{users[i].name}, {users[i].friends} friend(s)')

    print()

    # Quantidade de influencers
    influencers = 5

    mergeSort(users,0,len(users)-1)
    
    print('Influencers')
    for i in range(influencers):
        print(f'{users[i].name}, {users[i].friends} friends')