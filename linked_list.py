class Node:
	def __init__(self, data):
		self.val = data
		self.next = None

	def __str__(self):
		return str(self.val)

	def getData(self):
		return self.val

	def getNext(self):
		return self.next

	def setData(self, data):
		self.val = data

	def setNext(self, next):
		self.next = next


class LinkedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def __str__(self):
		current = self.head
		str_del = '->'

		list_str = ''
		while current is not None:
			list_str = list_str+str(current.getData())+str_del
			current = current.getNext()
		list_str = list_str[:-2]
		return list_str

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
		while current is not None:
			if current.getData() == item:
				found = True
			current = current.getNext()

		return found

	def add(self, item):
		t = Node(item)
		t.setNext(self.head)
		self.head = t
		return self.head

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while current is not None and found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

		return found

	def sumList(self,l2=None):
		current1 = self.head
		if l2:
			current2 = l2.head
		else:
			current2 = None
		head = None
		prev = None
		front_list = LinkedList()
		back_list = LinkedList()
		carry = 0
		while current1 is not None or current2 is not None:
			if current1:
				currData1 = current1.getData()
			else:
				currData1 = 0

			if current2:
				currData2 = current2.getData()
			else:
				currData2 = 0

			newVal = currData1 + currData2 + carry
			if carry == 1:
				carry = 0

			if newVal > 9:
				carry = 1
			newVal = newVal%10


			tail = Node(newVal)
			back_list.add(newVal)
			if head is None:
				head = tail
			else:
				prev.setNext(tail)
			prev = tail

			if current1:
				current1 = current1.getNext()
			if current2:
				current2 = current2.getNext()

		if carry:
			tail.next = Node(carry)
			back_list.add(carry)

		front_list.head = head
		return front_list, back_list

l1 = LinkedList()
print("Is empty? ", l1.isEmpty())
print("Adding elements...")
l1.add(9)
l1.add(7)
l1.add(2)
l1.add(4)
l1.add(8)
l1.add(1)
print("Is empty? ", l1.isEmpty())
print("How many elements? ", l1.count())
print("Is 1 in the list?", l1.search(1))
print("Removing 1...")
l1.remove(1)
print("How many elements? ", l1.count())
print("Is 1 in the list?", l1.search(1))
front, back = l1.sumList()
print("Frontward list:")
print(front)
print("Backward list:")
print(back)
