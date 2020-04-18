class Node():

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BTS():

    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._append(data, self.root)

    def _append(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._append(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._append(data, current_node.right)

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return is_found
            return False
        else:
            return None

    def _find(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        if data == current_node.data:
            return current_node.data
