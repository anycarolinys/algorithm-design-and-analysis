from NodeSequence import NodeSequence
# Retorna o tamanho máximo da subsequência mais longa
# estritamente crescente em uma sequência S
def LISlength(S,n):
  longest = 1
  S[0].lis = 1

  for j in range(1,n):
    S[j].lis = 1
    for k in range(0,j):
      lis = S[k].lis+1
      # Subsequência estritamente crescente
      if S[j].value >  S[k].value and S[j].lis < lis: 
          S[j].lis = lis
          if (lis > longest):
            longest = lis
  
  return longest

# Retorna os elementos que constituem a subsequência mais longa
# estritamente crescente em uma sequência S
def LISelements(S,n,longest):
  elements = [0] * longest
  
  for i in range(n,-1,-1):
    if S[i].lis == longest:
      elements[longest-1] = S[i].date
      # elements[longest-1] = S[i].value
      longest -= 1

  return elements

if __name__ == "__main__":

  # [800,900,850,955,750,1100,1215,1155]  
  V = [NodeSequence(800, "01/02/2021"),
      NodeSequence(900, "02/02/2021"),
      NodeSequence(850, "03/02/2021"),
      NodeSequence(955, "04/02/2021"),
      NodeSequence(750, "05/02/2021"),
      NodeSequence(1100, "06/02/2021"),
      NodeSequence(1005, "07/02/2021"),
      NodeSequence(1215, "08/02/2021"),
      NodeSequence(1155, "09/02/2021")]
  
  longest = LISlength(V,len(V))
  print(f"The length of the LIS is {longest}")
  print()

  for i in range(len(V)):
    print(V[i].value,V[i].lis)
  
  print()
  print(LISelements(V,len(V)-1,longest))