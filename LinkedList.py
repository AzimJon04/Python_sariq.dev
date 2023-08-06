class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
    def getNext(self):
        return self.next
    def setNext(self, val):
        self.next = val
class Linked:
    def __init__(self):
        self.head = None

    def size(self):
        counter = self.head
        count = 0
        while counter:
            count += 1
            counter = counter.getNext()
        return count

    def add(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        """Append item to the end of the list"""
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.next
            pos += 1
        new_node = Node(item)
        if previous is None:
            new_node.setNext(current)
            self.head = new_node
        else:
            previous.setNext(new_node)
    def inser(self, old_val, new_val):
        court = self.head
        perv = None
        while court:
            if court.data == old_val:
                perv = court.next
                court.next = new_val
                court = perv
            court = court.next

    def show(self):
        counter = self.head
        while counter:
            print(counter.data)
            counter = counter.next


if __name__ == "__main__":
    linked = Linked()
    linked.add("Dushanba")
    linked.append("Seshanba")
    linked.add("Yakshanba")
    linked.inser('Seshanba', 'Chorshanba')
    # print(linked.head.next.data)
    linked.show()