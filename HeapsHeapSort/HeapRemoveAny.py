''' Elabore um algoritmo para encontrar e remover um elemento arbitrário v em H, mantendo a propriedade de heap máximo durante o processo de busca e remoção. Considere que v existe em H. '''

def swap(A,i,j):
  aux = A[i]
  A[i] = A[j]
  A[j] = aux

def heapifyUp(H,pos):
  parent = pos // 2

  while parent >= 0:
    if H[pos] > H[parent]:
      swap(H,pos,parent)
      pos = parent
      parent //= 2
    else:
      parent = -1

def heapifyDown(H,pos,n):
  child = pos*2 + 1

  while child < n-1:
    if H[child] < H[child+1]:
      child += 1

    if H[child] > H[pos]:
      swap(H,child,pos)
      pos = child
      child *= 2
    else:
      child = n
      
def removeElement(H,v,n):
  pos = 0
  for i in range(n):
    if (v == H[i]):
      pos = i
  
  if pos != n-1:
    swap(H,pos,n-1)

    H.pop()
    n -= 1

    parent = pos//2
    if H[pos] <= H[parent]:
      heapifyDown(H,pos,n)
    else:
      heapifyUp(H,pos)
  else:
    H.pop()
    n -= 1    
    
if __name__ == "__main__":
  H = [20,18,15,11,0,13,9,10,1]
  print(H)

  removeElement(H,18,len(H))
  print(H)

  removeElement(H,15,len(H))
  print(H)

  removeElement(H,9,len(H))
  print(H)
  
  removeElement(H,20,len(H))
  print(H)