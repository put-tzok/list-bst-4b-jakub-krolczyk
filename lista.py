class Node():

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = Node()
        

    def append(self, data):
        next_node = Node(data)
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = next_node

    def find(self, key):
        current_node = self.head

        while current_node is not None:
            if current_node.data == key:
                return current_node
            current_node = current_node.next
