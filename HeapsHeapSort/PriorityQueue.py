class PriorityQueue:
  def __init__(self):
    self.size = -1
    self.pq = []

  def swap(self,i,j):
    aux = self.pq[i]
    self.pq[i] = self.pq[j]
    self.pq[j] = aux

  def heapifyUp(self,pos):
    parent = pos // 2

    while parent >= 0:
      if self.pq[pos] > self.pq[parent]:
        self.swap(pos,parent)
        pos = parent
        parent //= 2
      else:
        parent = -1

  def heapifyDown(self,pos):
    child = pos*2 + 1

    while child < self.size:
      if self.pq[child] < self.pq[child+1]:
        child += 1

      if self.pq[child] > self.pq[pos]:
        self.swap(child,pos)
        pos = child
        child *= 2
      else:
        child = self.size

  def insert(self,element):
    self.size += 1
    self.pq.append(element)
    self.heapifyUp(self.size)

  def extractMax(self):
    max = self.pq[0]

    self.pq[0] = self.pq[self.size]
    self.size -= 1
    self.pq.pop()

    self.heapifyDown(0)

    return max

  def maximumPriority(self):
    return self.pq[0]