class BinTree:
	def __init__(self, rootVal=None):
		self.rootVal = rootVal
		self.leftChild = None
		self.rightChild = None
		self.rheight = 0
		self.lheight = 0
	def getLeftChild(self):
		return self.leftChild
	def getRightChild(self):
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

	def preorder(self, visited=[]):
		if self.getRootVal() != 'root':
			visited.append(self.getRootVal())
		if self.leftChild:
			self.leftChild.preorder()
		if self.rightChild:
			self.rightChild.preorder()
		return visited

	def inorder(self, visited=[]):
		if self.leftChild:
			self.leftChild.inorder()
		if self.getRootVal() != 'root':
			visited.append(self.getRootVal())
		if self.rightChild:
			self.rightChild.inorder()
		return visited

	def postorder(self, visited=[]):
		if self.leftChild:
			self.leftChild.postorder()
		if self.rightChild:
			self.rightChild.postorder()
		if self.getRootVal() != 'root':
			visited.append(self.getRootVal())
		return visited


""" 

T1:

          0
        /   \
       /     \
      1       2
     / \     / \
    3   4   5   6


T2: T1 Reflective

          0
        /   \
       /     \
      2       1
     / \     / \
    6   5   4   3

"""
th = 2
c = th + 1
num_items = 2**(c) - 1
rv1 = list(range(num_items))
rv2 = list(range(num_items))

tree1 = BinTree(rv1[0])
tree2 = BinTree(rv2[0])

print("\nIN TREE T1:\n")
value_index_counter = 1
stack = []
for i, item in enumerate(rv1[1:]):
	if i == 0:
		next_roots = ['leftChild', 'rightChild']
		print(value_index_counter, item, next_roots[0])
		print(value_index_counter+1, rv1[value_index_counter+1], next_roots[1])
		exec("tree1.leftChild = BinTree(%d)"%item)
		exec("tree1.rightChild = BinTree(%d)"%(rv1[value_index_counter+1]))
		stack.extend(next_roots)		
		value_index_counter += 2
	else:
		next_root = stack.pop(0)
		next_roots = [next_root+'.'+'leftChild', next_root+'.'+'rightChild' ]
		for j, root in enumerate(next_roots):
			if value_index_counter >= len(rv1):
				break
			print(value_index_counter, rv1[value_index_counter], root)
			exec("tree1.%s = BinTree(%d)"%(root, rv1[value_index_counter]))
			value_index_counter += 1
		stack.extend(next_roots)

print("\nMIRROR TREE T2:\n")
value_index_counter = 1
stack = []
for i, item in enumerate(rv2[1:]):
	if i == 0:
		next_roots = ['rightChild', 'leftChild']
		print(value_index_counter, item, next_roots[0])
		print(value_index_counter+1, rv2[value_index_counter+1], next_roots[1])
		exec("tree2.rightChild = BinTree(%d)"%(rv2[value_index_counter]))
		exec("tree2.leftChild = BinTree(%d)"%(rv2[value_index_counter+1]))
		stack.extend(next_roots)		
		value_index_counter += 2
	else:
		next_root = stack.pop(0)
		next_roots = [next_root+'.'+'rightChild', next_root+'.'+'leftChild' ]
		for j, root in enumerate(next_roots):
			if value_index_counter >= len(rv2):
				break
			print(value_index_counter, rv2[value_index_counter], root)
			exec("tree2.%s = BinTree(%d)"%(root, rv2[value_index_counter]))
			value_index_counter += 1
		stack.extend(next_roots)

print("\nT1 height: %d"% tree1.height())
print("\nT2 height: %d"% tree2.height())

t1_pre = tree1.preorder()
t2_post = tree2.postorder()

print("\nT1 PRE-ORDER:")
print(t1_pre)
print("\nT2 POST-ORDER + REVERSE:")
print(t2_post[::-1])
if t2_post[::-1] == t1_pre:
	print("\nMIRROR: TRUE")
else:
	print("\nMIRROR: FALSE")

