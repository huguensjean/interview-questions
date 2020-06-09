# verba volant, scripta mannent

class MaxHeap:
	def __init__(self):
		self.heaplist = [0]
		self.currentSize = 0

	def __str__(self):
		return str(self.heaplist[1:])

	def size(self):
		return self.currentSize

	def insert(self, k):
		self.heaplist.append(k)
		self.currentSize = self.currentSize + 1
		self.perCup(self.currentSize)

	def perCup(self, i):
		while i//2 > 0:
			if self.heaplist[i] > self.heaplist[i//2]:
				t = self.heaplist[i]
				self.heaplist[i] = self.heaplist[i//2]
				self.heaplist[i//2] = t
			i = i//2

	def perDown(self, i):
		while i*2 <= self.currentSize:
			mc = self.maxChild(i)
			if self.heaplist[i] < self.heaplist[mc]:
				t = self.heaplist[mc]
				self.heaplist[mc] = self.heaplist[i]
				self.heaplist[i] = t
			i = mc

	def maxChild(self, i):
		if 2*i+1 > self.currentSize:
			return 2*i
		else:
			if self.heaplist[2*i] < self.heaplist[2*i+1]:
				return 2*i+1
			else:
				return 2*i

	def delMax(self):
		retVal = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentSize]
		self.heaplist.pop()
		self.currentSize = self.currentSize - 1
		self.perDown(1)
		return retVal

	def buildHeap(self, alist):
		i = len(alist) * 2
		self.currentSize = len(alist)
		self.heaplist = [0] + alist[:]
		while i > 0:
			self.perDown(i)
			i = i-1

myheap = MaxHeap()
l = [5,8,3,9,1,6,7, 67,2, 10, 11, 45, 23, 32, 22, 4, 15, 26]
myheap.buildHeap(l)
print(myheap)
for i in l:
	myheap.delMax()
	print(myheap)
for i in l:
	myheap.insert(i)
print(myheap)

