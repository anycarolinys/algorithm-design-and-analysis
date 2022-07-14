import string

def generateAlphabet(m):
  
  dic = {}
  alphabet = list(string.ascii_lowercase)
  alphabet.append(' ')
  for letter in alphabet:
    dic[letter] = m

  return dic

def shiftTable(P,m):
  dic = generateAlphabet(m)

  for j in range(0,m-1): #[0..m-2]
    dic[P[j]] = m-1-j

  return dic

def Horspool(T,n,P,m,dic):
  # dic = shiftTable(P,m)
  i = m-1

  numOcurrences = 0
  while i < n:
    k = 0
    while k < m and (P[m-1-k] == T[i-k]):
      k += 1
    if k == m:
      # print(i-m+1)
      numOcurrences += 1
      i += m
    else:
      i += dic[T[i]]

  return numOcurrences

def findOcurrences(T,k,P,m):
  
  highest = -1
  i = 0
  indexes = {}
  dic = shiftTable(P,m)
  for i in range(k):
    ocurrence = Horspool(T[i],len(T[i]),P,m,dic)
    print(f'Ocorrencias no texto {i}: {ocurrence}')

    if ocurrence > highest:
      highest = ocurrence
      # i eh o indice no vetor
      # i+1 eh o numero do texto
      indexes[highest] = [i]
    elif ocurrence == highest:
      indexes[highest].append(i)

  print('Texto(s) com maior(es) ocorrencia(s) =',indexes[highest])
  
if __name__ == "__main__":

  P = "casa"
  
  T0 = "nao ha house nessa frase" # 0
  
  T1 = "A casa dos recem-casados eh bonita" # 2

  T2 = "O casamento ocorreu na casa de praia."# 2

  T3 = "Quem casa, quer casa." # 2

  T4 = "Mi casa es su casa, pero su casa no es mi casa." #4

  T5 = "casasdnmisdnws casa iosdncasaoduinsq casadmadioawndmaioncasa" # 4

  T6 = "vou sair de casa amanha, comprar uma casa e casa" # 3

  T = [T0,T1,T2,T3,T4,T5,T6]

  findOcurrences(T,len(T),P,len(P))