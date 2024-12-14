# verba volant, scripta mannent

class MinHeap:
    """
    A MinHeap implementation using a list.
    The first element (index 0) is not used for convenience.
    """
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def __str__(self):
        # Print the heap elements (excluding the initial zero)
        return str(self.heaplist[1:])

    def size(self):
        return self.currentSize

    def insert(self, k):
        """
        Insert a new element k into the heap.
        """
        self.heaplist.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        """
        Move the element at index i up to its proper position in the heap.
        """
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                # Swap with parent
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i = i // 2

    def percDown(self, i):
        """
        Move the element at index i down to its proper position in the heap.
        """
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                # Swap with min child
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def minChild(self, i):
        """
        Return the index of the smallest child of the node at index i.
        """
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        else:
            if self.heaplist[2 * i] < self.heaplist[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def delMin(self):
        """
        Remove and return the smallest element from the heap.
        """
        if self.currentSize == 0:
            return None
        retVal = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.heaplist.pop()
        self.currentSize -= 1
        if self.currentSize > 0:
            self.percDown(1)
        return retVal

    def buildHeap(self, alist):
        """
        Build a heap from an existing list of items.
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1


if __name__ == "__main__":
    # Example usage
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print("\nOriginal list:")
    print(l)

    myheap = MinHeap()
    myheap.buildHeap(l)

    print("\nHeapsort Min:")
    myheap2 = MinHeap()
    myheap2.buildHeap(l)
    for _ in range(myheap2.size()):
        print(myheap2.delMin())

    print("\nGet all pairs in the list that add to 20")
    target = 20
    print("\nTarget sum: ", target)
    sum_tuple_list = []

    # Use the heap to find unique pairs that sum to target
    # We'll repeatedly take the smallest element and look for a complement in the rest.
    # This approach is O(n^2), but we maintain the original logic.
    while myheap.size() > 1:  # Need at least two elements to form a pair
        num1 = myheap.heaplist[1]
        for num2 in myheap.heaplist[2:]:
            if num1 + num2 == target:
                pair = tuple(sorted((num1, num2)))
                if pair not in sum_tuple_list:
                    sum_tuple_list.append(pair)
        myheap.delMin()

    print("\nInteger pairs:")
    print(sum_tuple_list)
