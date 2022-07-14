''' Suponha que sua entrada seja um vetor de n registros contendo (cpf, nome, gênero,
idade). Adapte o HeapSort para ordenar este vetor de acordo com a idade, em ordem
decrescente. Caso várias pessoas possuam a mesma idade, o desempate se dará pelo
gênero, de forma que pessoas de uma mesma idade do gênero feminino precedam as do
gênero masculino de mesma idade e, por sua vez, estas precedam as dos demais gêneros
de mesma idade. Você pode usar os símbolos 'F', 'M' e 'X', para designar os gêneros
feminino, masculino e demais gêneros, respectivamente. '''

from collections import namedtuple

def HeapSort(A):
  size = len(A)
  BuildMinHeap(A,size)
  
  for i in range(size-1,0,-1):
    swap(A,0,i)
    MinHeapify(A,0,i)
    
def BuildMinHeap(A,size):
  middle = size // 2 # piso da divisão

  for i in range(middle-1,-1,-1):
    MinHeapify(A,i,size)

def swap(A,i,j):
  aux = A[i]
  A[i] = A[j]
  A[j] = aux

def sortByGender(i,gender1,j,gender2):
  lowest = 0
  if gender1 == 'X' or gender1 == 'M' and gender2 == 'F':
    lowest = i
  else:
    lowest = j
  
  return lowest

def MinHeapify(A,i,size):
  left = 2*i + 1
  right = left + 1
  lowest = i

  if left < size and A[left].age < A[lowest].age:
    lowest = left

  if right < size and A[right].age < A[lowest].age:
    lowest = right

  if left < size and A[left].age == A[lowest].age and A[left].gender != A[lowest].gender:
    # if A[left].gender == 'X':
    #   lowest = left
    # elif A[left].gender == 'M' and A[lowest].gender == 'F':
    #   lowest = left
    lowest = sortByGender(left,A[left].gender,lowest,A[lowest].gender)
      
  if right < size and A[right].age == A[lowest].age and A[right].gender != A[lowest].gender:
    # if A[right].gender == 'X':
    #   lowest = right
    # elif A[right].gender == 'M' and A[lowest].gender == 'F':
    #   lowest = right
    lowest = sortByGender(right,A[right].gender,lowest,A[lowest].gender)
    

  if lowest != i:
    swap(A,i,lowest)
    MinHeapify(A,lowest,size)

Person = namedtuple('Person', ['cpf','name','gender','age'])

if __name__ == "__main__":
  p1 = Person('1234','Any','F',19)  
  p2 = Person('1235','Beatriz','X',19)
  p3 = Person('1236','Carlos','M',20)
  p4 = Person('1237','Joao','X',23)
  p5 = Person('1238','Daniela','F',27)
  p6 = Person('1239','Julia','F',20)
  p7 = Person('5429','Marcela','F',35)
  p8 = Person('8750','Linn','X',42)
  p9 = Person('8750','Sol','X',40)
  p10 = Person('8750','Arthur','M',55)
  p11 = Person('8750','Mario','X',55)
  p12 = Person('8750','Ariel','X',27)
  p13 = Person('8750','Rafa','M',27)

  peopleArray = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
  HeapSort(peopleArray)

  print()
  for i in range(len(peopleArray)):
    print(peopleArray[i].name, peopleArray[i].age, peopleArray[i].gender)