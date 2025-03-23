class Queue:
    def __init__(self):
        self.list_ = []

    def is_empty(self):
        if self.list_:
            return False
        return True

    def enqueue(self, data):
        self.list_.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        else:
            self.list_.pop(0)

    def get_front(self):
        if self.is_empty():
            raise IndexError
        else:
            print(self.list_[-1])

    def get_rear(self):
        if self.is_empty():
            raise IndexError

        else:
            print(self.list_[0])

    def size(self):
        print(len(self.list_))

    def show(self):
        return self.list_


q = Queue()
q.enqueue(1)
q.enqueue(22)
q.enqueue(12)
q.get_rear()
q.get_front()
print(q.show())
q.dequeue()
q.size()
print(q.show())

