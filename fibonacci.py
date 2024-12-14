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
        # Loop until we find the item or reach the end of the list
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:  # Item not found
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

        while current1 is not None or current2 is not None:
            currData1 = current1.getData() if current1 else 0
            currData2 = current2.getData() if current2 else 0

            newVal = currData1 + currData2 + carry
            carry = newVal // 10
            newVal = newVal % 10

            # Add to back_list in reverse (via add)
            front_list.add(newVal)

            # Create a forward list for back_list
            new_node = Node(newVal)
            if head is None:
                head = new_node
            else:
                prev.setNext(new_node)
            prev = new_node

            if current1:
                current1 = current1.getNext()
            if current2:
                current2 = current2.getNext()

        if carry:
            # If there's a remaining carry
            front_list.add(carry)
            new_node = Node(carry)
            if prev is not None:
                prev.setNext(new_node)
            else:
                head = new_node

        back_list.head = head
        return front_list, back_list

    def fibonacci(self, size=0, lucas=0):
        # If lucas = 2, start sequence as Lucas (2,1,...)
        # Otherwise standard Fibonacci (0,1,...)
        if lucas == 2:
            start = 2
            next_val = 1
        else:
            start = 0
            next_val = 1

        l2 = LinkedList()
        if size > 0:
            l2.add(start)   # Adds at head, so reversed order
        if size > 1:
            l2.add(next_val)

        for _ in range(size - 2):
            out_sum = start + next_val
            l2.add(out_sum)  # again, reversed insertion
            start = next_val
            next_val = out_sum

        # Now l2 has the sequence in reverse order
        current2 = l2.head
        front_list = LinkedList()
        back_list = LinkedList()

        head = None
        prev = None

        # front_list: build from current2 by adding at head (keeps reversed order)
        # back_list: build forward by linking nodes in correct order
        while current2 is not None:
            newVal = current2.getData()
            front_list.add(newVal)
            new_node = Node(newVal)
            if head is None:
                head = new_node
            else:
                prev.setNext(new_node)
            prev = new_node
            current2 = current2.getNext()

        back_list.head = head
        return front_list, back_list


# Example usage
if __name__ == "__main__":
    l1 = LinkedList()
    front, back = l1.fibonacci(10)
    print("\nFIBONACCI SERIES:")
    print("Frontward: ")
    print(front)
    print("Backward: ")
    print(back)
