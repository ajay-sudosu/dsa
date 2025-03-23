class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BT:
    def __init__(self, root=None):
        self.root = None

    def _insert(self, data, root):
        if root is None:
            return Node(data)
        if root.data > data:
            root.left = self._insert(data, root.left)

        else:
            root.right = self._insert(data, root.right)

        return root

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.data)
            self._inorder(root.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root:
            result.append(root.data)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.data)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _min_value(self, root):
        if not root.left:
            return root.data
        return self._min_value(root.left)

    def min_value(self):
        return self._min_value(self.root)

    def _max_value(self, root):
        if not root.right:
            return root.data
        return self._max_value(root.right)

    def max_value(self):
        return self._max_value(self.root)

    def _delete(self, root, data):
        if root is None:
            return root

        if data > root.data:
            root.right = self._delete(root.right, data)

        elif data < root.data:
            root.left = self._delete(root.left, data)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self.min_value()
            self._delete(root.right, root.data)

        return root

    def delete(self, data):
        self.root = self._delete(self.root, data)


bt = BT()
bt.insert(1034)
bt.insert(60)
bt.insert(602)
bt.insert(4460)
bt.insert(6230)
bt.insert(1000)
print(bt.inorder())
print(bt.min_value())
print(bt.max_value())
print(bt.inorder())
bt.delete(1000)
print(bt.inorder())

