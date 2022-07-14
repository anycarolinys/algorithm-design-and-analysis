def computesNext(P,m):
  next = [0] * m
  i = 1
  j = 0

  next[0] = 0

  # O padrao eh percorrido no intervalo [1..m]
  while i < m:
    if P[i] == P[j]:
      # Se houver um match
      # soma o valor da posicao que deu 
      # match mais 1
      # o +1 eh necessario pq a indexacao do array 
      # eh sempre 1 a menos do que a posicao real
      next[i] = j+1
      # Havendo um match deve-se avançar
      # na posicao mais anterior (j) na qual houve match 
      j += 1
      # Havendo um match deve-se avançar
      # na posicao mais posterior (i) na qual houve match
      i += 1
    else:
      # Deve-se testar se o indexador j
      # chegou ao inicio do vetor 
      
      # Se nao chegou no inicio do vetor
      # basta o indexador mais anterior (j)
      # adquira o valor de next da posicao anterior a ele
      # para ir para a posicao exata onde o match pode possivelmente ocorrer
      # esse processo pode acontecer ate j ser igual a 0
      if j != 0:
        j = next[j-1]
      else:
        # Se nao houver match e se o apontador j
        # estiver no inicio do vetor
        # naquela posicao nao houve possibilidade de match
        # com nenhum prefixos
        next[i] = 0
        # O apontador do posterior pode avançar para a proxima
        # letra
        i += 1
  
  return next

def KMP(T,n,P,m):
  next = computesNext(P,m)

  # print(next)
  i = 0
  j = 0
  
  numOcurrences = 0
  # index = -1
  while i < n:
    if T[i] == P[j]:
      i += 1
      j += 1
    else:
      if j != 0:
        j = next[j-1]
      else:
        i += 1

    if j == m:
      # print(i-j)
      # index = i-j
      numOcurrences += 1
      j = next[j-1]

  return numOcurrences

def findOcurrences(T,k,P,m):
  
  highest = -1
  i = 0
  indexes = {}
  
  for i in range(k):
    ocurrence = KMP(T[i],len(T[i]),P,m)
    print(f'Ocorrencias no texto {i}: {ocurrence}')

    if ocurrence > highest:
      highest = ocurrence
      indexes[highest] = [i]
    elif ocurrence == highest:
      indexes[highest].append(i)
          
  print('Maior(es) ocorrencia(s) =',indexes[highest])

if __name__ == "__main__":
  
  P = "casa"
  
  T0 = "nao ha house nessa frase" # 0
  
  T1 = "A casa dos recem-casados eh bonita" # 2

  T2 = "O casamento ocorreu na casa de praia."# 2

  T3 = "Quem casa, quer casa." # 2

  T4 = "Mi casa es su casa, pero su casa no es mi casa."

  T5 = "casasdnmisdnws casa iosdncasaoduinsq casadmadioawndmaioncasa" # 4

  T6 = "vou sair de casa amanha, comprar uma casa e casa" # 3

  T = [T0,T1,T2,T3,T4,T5,T6]

  findOcurrences(T,len(T),P,len(P))