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
        self.currentSize += 1
        self.perCup(self.currentSize)

    def perCup(self, i):
        # Move the element at index i up until heap property is restored
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                # Swap
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i = i // 2

    def perDown(self, i):
        # Move the element at index i down until heap property is restored
        while i * 2 <= self.currentSize:
            mc = self.maxChild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def maxChild(self, i):
        # Return the index of the larger child
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        else:
            if self.heaplist[2 * i] < self.heaplist[2 * i + 1]:
                return 2 * i + 1
            else:
                return 2 * i

    def delMax(self):
        # Remove and return the maximum element
        retVal = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.heaplist.pop()
        self.currentSize -= 1
        if self.currentSize > 0:
            self.perDown(1)
        return retVal

    def buildHeap(self, alist):
        # Build a heap from an unsorted list
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        i = len(alist) // 2
        while i > 0:
            self.perDown(i)
            i -= 1


if __name__ == "__main__":
    myheap = MaxHeap()
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print("\nOriginal list:")
    print(l)
    myheap.buildHeap(l)

    print("\nHeapsort Max:")
    myheap2 = MaxHeap()
    myheap2.buildHeap(l)
    sorted_desc = []
    for _ in range(myheap2.currentSize):
        sorted_desc.append(myheap2.delMax())
    print(sorted_desc)

    # Find all unique pairs that add to 20
    print("\nGet all pairs in the list that add to 20")
    target = 20
    print("\nTarget sum:", target)

    # We'll use the heap as given: each time taking the max and comparing it with others
    sum_tuple_list = []
    temp_heap = MaxHeap()
    temp_heap.buildHeap(l)

    while temp_heap.size() > 0:
        num1 = temp_heap.heaplist[1]
        # Check pairs with remaining elements
        for n in temp_heap.heaplist[2:]:
            num2 = n
            if num1 + num2 == target:
                pair = tuple(sorted((num1, num2)))
                if pair not in sum_tuple_list:
                    sum_tuple_list.append(pair)
        temp_heap.delMax()

    print("\nInteger pairs:")
    print(sum_tuple_list)
