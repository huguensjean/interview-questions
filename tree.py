class BinTree:
    def __init__(self, rootVal=None):
        self.rootVal = rootVal
        self.leftChild = None
        self.rightChild = None

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
        left_height = self.leftChild.height() + 1 if self.leftChild else 0
        right_height = self.rightChild.height() + 1 if self.rightChild else 0
        return max(left_height, right_height)

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

    def spinLeaves(self):
        # This logic remains as given, assuming it works as intended.
        if self.leftChild and self.rightChild:
            if self.rightChild.getRootVal() != 'X' or self.leftChild.getRootVal() != 'X':
                tval = self.rightChild.getRootVal()
                self.rightChild.setRootVal(self.leftChild.getRootVal())
                self.leftChild.setRootVal(tval)

        if self.leftChild and not self.rightChild:
            self.rightChild = self.leftChild
            self.leftChild = BinTree('X')

        if self.rightChild and not self.leftChild:
            self.leftChild = self.rightChild
            self.rightChild = BinTree('X')

        if self.leftChild:
            self.leftChild.spinLeaves()
        if self.rightChild:
            self.rightChild.spinLeaves()

        if self.leftChild and self.leftChild.getRootVal() == 'X':
            self.leftChild = None
        if self.rightChild and self.rightChild.getRootVal() == 'X':
            self.rightChild = None

    def preorder(self):
        visited = []
        self._preorder(visited)
        return visited

    def _preorder(self, visited):
        if self.getRootVal() != 'root':
            visited.append(self.getRootVal())
        if self.leftChild:
            self.leftChild._preorder(visited)
        if self.rightChild:
            self.rightChild._preorder(visited)

    def inorder(self):
        visited = []
        self._inorder(visited)
        return visited

    def _inorder(self, visited):
        if self.leftChild:
            self.leftChild._inorder(visited)
        if self.getRootVal() != 'root':
            visited.append(self.getRootVal())
        if self.rightChild:
            self.rightChild._inorder(visited)

    def postorder(self):
        visited = []
        self._postorder(visited)
        return visited

    def _postorder(self, visited):
        if self.leftChild:
            self.leftChild._postorder(visited)
        if self.rightChild:
            self.rightChild._postorder(visited)
        if self.getRootVal() != 'root':
            visited.append(self.getRootVal())


def buildTree(values, mirror=False):
    """
    Build a full binary tree from a list of values.
    If mirror=True, children are inserted in mirrored order:
    - For normal: leftChild, then rightChild
    - For mirror: rightChild, then leftChild
    """
    if not values:
        return None
    root = BinTree(values[0])
    nodes = [root]
    i = 1
    while i < len(values):
        current = nodes.pop(0)
        if mirror:
            # Insert right, then left
            if i < len(values):
                current.rightChild = BinTree(values[i])
                nodes.append(current.rightChild)
                i += 1
            if i < len(values):
                current.leftChild = BinTree(values[i])
                nodes.append(current.leftChild)
                i += 1
        else:
            # Insert left, then right
            if i < len(values):
                current.leftChild = BinTree(values[i])
                nodes.append(current.leftChild)
                i += 1
            if i < len(values):
                current.rightChild = BinTree(values[i])
                nodes.append(current.rightChild)
                i += 1
    return root


if __name__ == "__main__":
    th = 2
    c = th + 1
    num_items = 2**c - 1
    rv1 = list(range(num_items))
    rv2 = list(range(num_items))

    # Build T1 (normal) and T2 (mirror) trees
    tree1 = buildTree(rv1, mirror=False)
    tree2 = buildTree(rv2, mirror=True)

    print("\nT1 height:", tree1.height())
    print("T2 height:", tree2.height())

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

    print("\nNUMBER OF NODES:", num_items)
