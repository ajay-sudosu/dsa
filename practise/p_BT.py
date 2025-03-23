class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BT:
    def __init__(self, root=None):
        self.root = root

    def _insert(self, root, data):
        if root is None:
            return Node(data=data)
        if data > root.data:
            root.right = self._insert(root.right, data)
        else:
            root.left = self._insert(root.left, data)
        return root

    def _show(self, root, result):
        if root:
            self._show(root.left, result)
            result.append(root.data)
            self._show(root.right, result)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def show(self):
        result = []
        self._show(self.root, result)
        return result


bt = BT()
bt.insert(10)
bt.insert(200)
bt.insert(110)
bt.insert(610)
bt.insert(410)
print(bt.show())
