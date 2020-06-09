import timeit
import random

class Node:
	def __init__(self, item):
		self.data = item
		self.next = None
	def getData(self):
		return self.data
	def __str__(self):
		return str(self.data)
	def getNext(self):
		return self.next
	def setData(self, item):
		self.data = item
	def setNext(self, node):
		self.next = node


class OrderedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None

	def __str__(self):
		current = self.head
		startStr = ''
		while current is not None:
			startStr += ' '+str(current.getData())
			current = current.getNext()
		return startStr.lstrip()

	def count(self):
		current = self.head
		count = 0
		while current is not None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current is not None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found
	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current is not None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous is None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while current is not None and not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous is None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())


def getRandomList():
	randomlist = []
	for i in range(0, 16):
		n = random.randint(1, 20)
		randomlist.append(n)
	return randomlist

def sortList(listNum, ordered_list=OrderedList()):
	pos = 0
	if len(listNum) == 1:
		ordered_list.add(listNum[0])
		return ordered_list
	else:
		ordered_list.add(listNum[0])
		return sortList(listNum[1:], ordered_list)


def mergeSortList(listNum, temp_list=[], ordered_list=OrderedList()):
	if len(temp_list) == 0 and len(listNum) > 0:
		midpoint = len(listNum)//2
		temp_list = listNum[midpoint:]
		listNum = listNum[:midpoint]
	if len(listNum) == 0:
		return ordered_list
	else:
		ordered_list.add(listNum[0])
		if len(temp_list):
			ordered_list.add(temp_list[0])
		return mergeSortList(listNum[1:], temp_list[1:], ordered_list)

def main():

	listNum = getRandomList()
	print("Original list: \n", listNum)
	print(len(listNum))
	#print()
	#print("Python Sorted list: \n", sorted(listNum))
	print()
	sortedList = mergeSortList(listNum)
	print("Sorted list:\n")
	print(sortedList)
	print(sortedList.count())

print("execution time:", timeit.timeit(main, number=1))
