class Node:
    def __init__(self, data, prev_ref=None, next_ref=None):
        self.data = data
        self.prev_ref = prev_ref
        self.next_ref = next_ref


class DQ:
    def __init__(self, front=None, rear=None):
        self.rear = rear
        self.front = front
        self.count = 0

    def insert_single_node(self, data):
        new_node = Node(data=data)
        self.front = self.rear = new_node

    def insert_front(self, data):
        if not self.is_empty():
            new_node = Node(data=data, next_ref=self.front)
            self.front.prev_ref = new_node
            self.front = new_node
        else:
            self.insert_single_node(data)
        self.count += 1

    def insert_last(self, data):
        if not self.is_empty():
            new_node = Node(data=data, prev_ref=self.rear)
            self.rear.next_ref = new_node
            self.rear = new_node
        else:
            self.insert_single_node(data=data)
        self.count += 1

    def remove_single_node(self):
        self.front = self.rear = None

    def delete_front(self):
        if not self.is_empty():
            if self.front.next_ref:
                self.front.next_ref.prev_ref = None
                self.front = self.front.next_ref
            else:
                self.remove_single_node()
            self.count -= 1
        else:
            print("empty")

    def delete_last(self):
        if not self.is_empty():
            if self.front.next_ref:
                self.rear.prev_ref.next_ref = None
                self.rear = self.rear.prev_ref
            else:
                self.remove_single_node()
            self.count -= 1
        else:
            print("empty")

    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("Empty")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            print("Empty")

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def show(self):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next_ref
            print()


dq = DQ()
dq.insert_front(20)
dq.insert_front(10)
dq.insert_last(40)
dq.show()
dq.delete_last()
dq.delete_last()
dq.delete_last()
dq.show()
print(dq.size())

