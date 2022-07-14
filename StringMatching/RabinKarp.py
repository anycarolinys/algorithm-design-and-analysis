q = 3354393
d = 32

def HashPattern(P, m):
  global q,d
  
  hash = 0
  
  for i in range(m):
    hash = (hash*d + ord(P[i])) % q

  return hash

def RabinKarp(T,n,P,k,m): # O(n + km)
  global q,d
  dM = 1

  # Obtendo as potencias da base d
  for i in range(0,m-1):
    dM = d*dM % q


  patternSet = {}
  # Calculando o hash dos padroes
  for i in range(k):
    pHash = HashPattern(P[i],m)
    patternSet[pHash] = P[i]
  
  textHash = 0

  # Hash dos 'm' primeiros caracteres do texto
  for i in range(m):
    textHash = (textHash*d + ord(T[i])) % q

  count = 0
  i = 0

  while i <= n-m:
    # Testa se o valor existe no conjunto 
    # de hashes dos padroes
    p =  patternSet.get(textHash) # Tempo costante
    if p is not None:
      count += 1

    if i+m < n:
      textHash = (textHash + (d*q) - (ord(T[i])*dM)) % q
      textHash = (textHash*d + ord(T[i+m])) % q
    i += 1

  return count

if __name__ == "__main__":

  T = "te adoro em tudo tudo em te adorar tu"
  n = len(T)
  P = ['te','ad','em','tu']
  k = len(P)
  m = len(P[0])

  count = RabinKarp(T,n,P,k,m)
  print(f'Os padroes {P} ocorrem {count} vezes')
  
  T = "top bom bem bomm bem osk etvasbut top"
  n = len(T)
  P = ['top','bem','bom']
  k = len(P)
  m = len(P[0])
  
  count = RabinKarp(T,n,P,k,m)
  print(f'Os padroes {P} ocorrem {count} vezes')
  
  T = "top bom bem bomm bem osk etvasbut top"
  n = len(T)
  P = ['nao','tem','bam']
  k = len(P)
  m = len(P[0])
  
  count = RabinKarp(T,n,P,k,m)
  print(f'Os padroes {P} ocorrem {count} vezes')