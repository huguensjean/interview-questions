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
        return self.head is None

    def __str__(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.getData()))
            current = current.getNext()
        return ' '.join(elements)

    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            # Since the list is ordered, stop if the current data exceeds the item
            if current.getData() > item:
                return False
            current = current.getNext()
        return False

    def add(self, item):
        current = self.head
        previous = None
        # Find the position to insert the new item
        while current is not None and current.getData() <= item:
            previous = current
            current = current.getNext()

        new_node = Node(item)
        if previous is None:
            # Insert at the head
            new_node.setNext(self.head)
            self.head = new_node
        else:
            # Insert after previous
            new_node.setNext(current)
            previous.setNext(new_node)

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

        if not found:
            # Item not found, do nothing or raise an error
            return

        if previous is None:
            # Removing the head
            self.head = current.getNext()
        else:
            # Removing from the middle or end
            previous.setNext(current.getNext())


def getRandomList(size=16, start=1, end=20):
    return [random.randint(start, end) for _ in range(size)]

def sortList(listNum):
    ordered_list = OrderedList()
    for item in listNum:
        ordered_list.add(item)
    return ordered_list

def main():
    listNum = getRandomList()
    print("Original list:")
    print(listNum)

    sortedList = sortList(listNum)
    print("\nSorted list:")
    # The OrderedList __str__ method returns space-separated values
    print(sortedList)

print("Execution time:", timeit.timeit(main, number=1))
