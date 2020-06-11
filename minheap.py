# verba volant, scripta mannent

class MinHeap:
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
			if self.heaplist[i] < self.heaplist[i//2]:
				t = self.heaplist[i // 2]
				self.heaplist[i // 2] = self.heaplist[i]
				self.heaplist[i] = t
			i = i//2

	def perDown(self, i):
		while i*2 <= self.currentSize:
			mc = self.minChild(i)
			if self.heaplist[i] > self.heaplist[mc]:
				t = self.heaplist[i]
				self.heaplist[i] = self.heaplist[mc]
				self.heaplist[mc] = t
			i = mc

	def minChild(self, i):
		if 2*i+1 > self.currentSize:
			return 2*i
		else:
			if self.heaplist[2*i] < self.heaplist[2*i+1]:
				return 2*i
			else:
				return 2*i+1

	def delMin(self):
		retVal = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentSize]
		self.heaplist.pop()
		self.currentSize = self.currentSize - 1
		self.perDown(1)
		return retVal

	def buildHeap(self, alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heaplist = [0] + alist[:]
		while i > 0:
			self.perDown(i)
			i = i -1

myheap = MinHeap()
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print("\nOriginal list:")
print(l)
myheap.buildHeap(l)

print("\nHeapsort Min")
myheap2 = MinHeap()
myheap2.buildHeap(l)
for i in range(myheap2.currentSize):
	print(myheap2.delMin())

print("\nGet all pairs in the list that add to 20")
num1 = num2 = 0
target = 20
print("\nTarget sum: ", target)
sum_tuple_list = []
for i in l:
	num1 = myheap.heaplist[1]
	for n in myheap.heaplist[2:]:
		num2 = n
		if num1 + num2 == target:
			pair = sorted((num1, num2))
			if pair not in sum_tuple_list:
				sum_tuple_list.append(tuple(pair))
	myheap.delMin()
print("\nInteger pairs:")
print(sum_tuple_list)


