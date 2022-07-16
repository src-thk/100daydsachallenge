class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.insert_at_start(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            new_node.next = None

    def insert_after(self, data, value):
        new_node = Node(data)
        current = self.head
        while current.data != value:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def insert_before(self, data, value):
        new_node = Node(data)
        current = self.head
        if current.data == value:
            self.insert_at_start(data)
        else:
            while current.next.data != value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_at_start(self):
        if self.head == None:
            raise RuntimeError("Cannot delete an empty LinkedList")
        else:
            current = self.head
            self.head = current.next

    def delete_at_end(self):
        if self.head == None:
            raise RuntimeError("Cannot delete an empty LinkedList")
        current = self.head
        if current.next == None:
            self.head == None
        else:
            while current.next.next != None:
                current = current.next
            current.next = None

    def delete_by_value(self, value):
        if self.head == None:
            raise RuntimeError("Cannot delete an empty LinkedList")
        previous = self.head
        if previous.data == value:
            self.head == None
        else:
            current = previous.next
            while current.data != value:
                previous = previous.next
                current = current.next
            previous.next = current.next

    @property
    def output(self):
        if self.head == None:
            raise Exception("LinkedList is empty!")
        else:
            current = self.head
            while current != None:
                print(current.data, end='->')
                current = current.next


ll = LinkedList()
ll.insert_at_end(2)
ll.insert_at_end(4)
ll.insert_at_start(1)
ll.insert_at_end(3)
ll.insert_after(9, 4)
ll.insert_before(8, 3)
ll.delete_at_start()
ll.delete_at_end()
ll.delete_by_value(9)
ll.output
