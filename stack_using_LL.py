class Node:
    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


class Stack:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        if not self.start:
            return True
        return False

    def push(self, data):
        new_node = Node(data=data, next_ref=self.start)
        self.start = new_node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.data
            self.start = self.start.next_ref
            self.count -= 1
            return data
        else:
            raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            print("Empty stack")

    def size(self):
        return self.count


s = Stack()
print(s.push(1))
print(s.push(20))
print(s.pop())
print(s.peek())
