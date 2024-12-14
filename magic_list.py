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
        list_str = []
        while current is not None:
            list_str.append(str(current.getData()))
            current = current.getNext()
        return '->'.join(list_str)

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

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            return False  # Item not in the list

        if previous is None:
            # Removing the head
            self.head = current.getNext()
        else:
            # Removing a non-head node
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
            val1 = current1.getData() if current1 else 0
            val2 = current2.getData() if current2 else 0

            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            sum_val = sum_val % 10

            # Add to front_list in forward order
            new_node = Node(sum_val)
            if head is None:
                head = new_node
                prev = new_node
            else:
                prev.setNext(new_node)
                prev = new_node

            # Add to back_list in reverse order
            back_list.add(sum_val)

            if current1:
                current1 = current1.getNext()
            if current2:
                current2 = current2.getNext()

        if carry > 0:
            # Add the carry at the end of both lists
            new_node = Node(carry)
            prev.setNext(new_node)
            back_list.add(carry)

        front_list.head = head
        return front_list, back_list


# Example Usage
if __name__ == "__main__":
    l1 = LinkedList()
    l1.add(9)
    l1.add(7)
    l1.add(2)
    l1.add(4)
    l1.add(8)
    l1.add(1)
    print("List 1:", l1)

    l2 = LinkedList()
    l2.add(1)
    l2.add(1)
    l2.add(1)
    l2.add(1)
    print("List 2:", l2)

    front, back = l1.sumList(l2)
    print("\nSum front (forward order):", front)
    print("Sum back (reverse order):", back)
