''' Considere um heap máximo H de n elementos.
Elabore um algoritmo para encontrar e remover o elemento de menor valor de H, mantendo a propriedade de heap máximo durante o processo de busca e remoção. '''
def MaxHeapify(A,i,size):
  leftChild = 2*i + 1
  rightChild = leftChild + 1
  largest = i

  if leftChild < size and A[leftChild] > A[largest]:
    largest = leftChild

  if rightChild < size and A[rightChild] > A[largest]:
    largest = rightChild

  if largest != i:
    swap(A,i,largest)
    MaxHeapify(A,largest,size)

def swap(A,i,j):
  aux = A[i]
  A[i] = A[j]
  A[j] = aux

def searchLowest(A):
  size = len(A)
  middle = size // 2

  lowest = middle

  for i in range(middle,size):
    if A[i] < A[lowest]:
      lowest = i

  return lowest

def removeLowest(A):
  lowest = searchLowest(A)

  size = len(A)-1
  print('Lowest = ',A[lowest])
  if (lowest != size):  
    swap(A,lowest,size)
    A.pop()
    size -= 1
    MaxHeapify(A,lowest,size)
  else:
    A.pop()
    size -= 1
    
if __name__ == "__main__":
  HM = [20,18,15,11,0,13,9,10,1]

  removeLowest(HM)

  print(HM)

  HM1 = [17,15,13,9,6,5,10,4,8,3,1]

  removeLowest(HM1)

  print(HM1)