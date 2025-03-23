class DQ:

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def append(self, data):
        new_node = Node(data=data)
        if self.is_empty():
            self.front = new_node

        else:
            self.rear.next_ref = new_node
            new_node.pre_ref = self.rear
        self.rear = new_node
        self.count += 1

    def append_front(self, data):
        new_node = Node(data=data)
        if not self.is_empty():
            self.front.pre_ref = new_node
            new_node.next_ref = self.front
            self.front = new_node

        else:
            self.front = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("Empty")

        else:
            if self.front.next_ref:
                self.rear.pre_ref.next_ref = None
                self.rear = self.rear.pre_ref
            else:
                self.front = self.rear = None
            self.count -= 1

    def pop_front(self):
        if self.is_empty():
            print("Empty")

        else:
            if not self.front.next_ref:
                self.front = self.rear = None

            else:
                self.front.next_ref.pre_ref = None
                self.front = self.front.next_ref
            self.count -= 1

    def show(self):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next_ref
            print()


class Node:
    def __init__(self, data, pre_ref=None, next_ref=None):
        self.next_ref = next_ref
        self.pre_ref = pre_ref
        self.data = data


dq = DQ()
dq.append(1)
dq.append(2)
dq.append(3)
dq.append_front(0)
dq.show()
dq.pop_front()
dq.pop_front()
dq.pop_front()
dq.pop_front()
dq.pop_front()
dq.pop_front()
dq.show()
