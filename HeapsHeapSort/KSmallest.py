''' Dado um vetor de n inteiros distintos em ordem arbitrária, elabore um algoritmo para encontrar o k-ésimo menor elemento do vetor. A complexidade da sua solução deve ser O(n log k). Você pode
usar um espaço adicional de tamanho k. '''

from PriorityQueue import PriorityQueue

def KSmallest(array,PQ,k):
  
  for i in range(len(array)):
    PQ.insert(array[i])
  
    if PQ.size >= k:
      r = PQ.extractMax()
      print(r)
  
  return PQ.maximumPriority()
  
if __name__ == "__main__":
  array = [5, 20, 10, 7, 1];
  # array = [5,9,10,11,15,18,24]
  
  PQ = PriorityQueue()
  k = 4
  result = KSmallest(array, PQ, k)
  print(PQ.pq)
  print(f'{result} é o {k}º menor elemento de {array}')