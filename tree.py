class BinTree:
	def __init__(self, rootVal=None):
		self.rootVal = rootVal
		self.leftChild = None
		self.rightChild = None
		self.rheight = 0
		self.lheight = 0
	def getLeftChild(self):
		return self.lelfChild
	def getrightChild(self):
		return self.rightChild
	def getRootVal(self):
		return self.rootVal
	def setRootVal(self, val):
		self.rootVal = val
	def height(self):
		if self.leftChild is None and self.rightChild is None:
			return 0
		else:
			if self.leftChild:
				self.lheight = self.leftChild.height() + 1
			if self.rightChild:
				self.rheight = self.rightChild.height() + 1

		return max([self.lheight, self.rheight])

	def insertLeft(self, item):
		if self.leftChild is None:
			self.leftChild = BinTree(item)
		else:
			t = BinTree(item)
			t.leftChild = self.leftChild
			self.leftChild = t
	def insertRight(self, item):
		if self.rightChild is None:
			self.rightChild = BinTree(item)
		else:
			t = BinTree(item)
			t.rightChild = self.rightChild
			self.rightChild = t

	def preorder(self):
		print(self.getRootVal())
		if self.leftChild:
			self.leftChild.preorder()
		if self.rightChild:
			self.rightChild.preorder()

	def inorder(self):
		if self.leftChild:
			self.leftChild.inorder()
		print(self.getRootVal())
		if self.rightChild:
			self.rightChild.inorder()

	def postorder(self):
		if self.leftChild:
			self.leftChild.postorder()
		if self.rightChild:
			self.rightChild.postorder()
		print(self.getRootVal())

l1 = list(range(10))
l2 = l1[::-1]
tree = BinTree()
print("ORIGINAL L1", len(l1))
for i in l1:
	print(i)
	tree.insertLeft(i)

print("ORIGINAL L2", len(l2))
for i in l2:
	print(i)
	tree.insertRight(i)

print("PREORDER")
tree.preorder()
print("INORDER")
tree.inorder()
print("POSTORDER")
tree.postorder()
print("HEIGHT")
print(tree.height())
