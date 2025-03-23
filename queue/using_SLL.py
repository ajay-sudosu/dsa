class Node:
    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


class Queue:
    def __init__(self, rear=None, front=None):
        self.rear = rear
        self.front = front
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data):
        new_node = Node(data=data)
        if self.is_empty():
            self.front = new_node

        else:
            self.rear.next_ref = new_node
        self.rear = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError

        else:
            if self.count == 1:
                data = self.rear.data
                self.rear = self.front = None
                return data
            else:
                self.front = self.front.next_ref
            self.count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError
        else:
            return self.front.data

    def get_rear(self):
        if self.is_empty():
            raise IndexError

        else:
            return self.rear.data

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


q = Queue()
q.enqueue(1)
q.enqueue(100)
q.enqueue(223)
q.enqueue(12422)
q.enqueue(4312)
print(q.get_rear())
print(q.get_front())
q.show()
q.dequeue()
q.show()
print(q.size())

