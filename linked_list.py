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

    def setNext(self, nxt):
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        if self.head is None:
            return ''
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.getData()))
            current = current.getNext()
        return '->'.join(elements)

    def count(self):
        current = self.head
        cnt = 0
        while current is not None:
            cnt += 1
            current = current.getNext()
        return cnt

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def add(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
        return self.head

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        # Search for the item
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            # Item not found in the list
            return False

        # If removing the head
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return True

    def sumList(self, l2=None):
        current1 = self.head
        current2 = l2.head if l2 else None

        front_list = LinkedList()
        back_list = LinkedList()

        carry = 0
        head = None
        prev = None

        # Add corresponding nodes and carry
        while current1 is not None or current2 is not None:
            val1 = current1.getData() if current1 else 0
            val2 = current2.getData() if current2 else 0

            newVal = val1 + val2 + carry
            carry = newVal // 10
            newVal = newVal % 10

            # Build the front_list in forward order
            new_node = Node(newVal)
            if head is None:
                head = new_node
            else:
                prev.setNext(new_node)
            prev = new_node

            # Build the back_list in reverse order
            back_list.add(newVal)

            if current1:
                current1 = current1.getNext()
            if current2:
                current2 = current2.getNext()

        # If there's a remaining carry
        if carry > 0:
            prev.setNext(Node(carry))
            back_list.add(carry)

        front_list.head = head
        return front_list, back_list


# Example usage
if __name__ == "__main__":
    l1 = LinkedList()
    print("Is empty?", l1.isEmpty())
    print("Adding elements...")
    l1.add(9)
    l1.add(7)
    l1.add(2)
    l1.add(4)
    l1.add(8)
    l1.add(1)
    print("Is empty?", l1.isEmpty())
    print("How many elements?", l1.count())
    print("Is 1 in the list?", l1.search(1))
    print("Removing 1...")
    l1.remove(1)
    print("How many elements?", l1.count())
    print("Is 1 in the list?", l1.search(1))
    front, back = l1.sumList()
    print("Frontward list:")
    print(front)
    print("Backward list:")
    print(back)
