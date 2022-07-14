''' Você foi requisitado a elaborar um algoritmo para
identificar as cem pessoas mais influentes da rede, a fim de engajá-las numa campanha
publicitária. A agência dispõe de um arquivo cujos registros incluem o nome da pessoa
e a quantidade de amigos que ela possui na rede. A pessoa x é mais influente que a
pessoa y se o número de amigos de x for maior que o número de amigos de y, na rede
social. Você pode supor que os dados do arquivo cabem em memória primária. Se duas
ou mais pessoas forem igualmente influentes, você pode escolher arbitrariamente entre
elas quando estiver coletando os últimos dados. '''
import random
import collections

User = collections.namedtuple('User', ['name', 'friends'])

def swap(v, max, n):
  # Variavel auxiliar recebe 
  # ultimo elemento
  aux = v[n] 
  # Elemento maximo atribuido 
  # a ultima posicao do vetor
  v[n] = v[max]
  # Antiga posicao do valor maximo
  # recebe o ultimo valor do vetor
  v[max] = aux
  
def maxFriends(users:User, n):
  if n == 0: # Caso base
    return 0

  maximum = maxFriends(users, n-1) # HI

  if users[n].friends > users[maximum].friends: # Caso geral
    maximum = n

  return maximum


if __name__ == "__main__":

  # Quantidade de usuarios da rede social
  n = 10
  # Gerando lista com os dados dos usuarios
  users = [ [] for i in range(n)] 

  # Gerando aleatoriamente nome e quantidade 
  # de amigos para os usuarios
  for i in range(n):
    # Considerando que o usuario tem, no minimo, um amigo
    r = random.randint(1, i+1) 
    name = 'Name'+ str(i)
    friends = r
    users[i] = User(name, friends)

  # Imprimindo todos os usuarios da rede social
  for j in range(n):
    print(f'{users[j].name}, {users[j].friends} friend(s)')

  print()

  lenUsers = len(users)
  # Quantidade de influencers
  influencers = 5
  
  for i in range(1, influencers+1):
    maxUserFriend = maxFriends(users, lenUsers-i)
    swap(users, maxUserFriend, lenUsers-i)
    print(f'Influencer {users[lenUsers-i].name}, {users[lenUsers-i].friends} friend(s)')