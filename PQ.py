class PQ:
    def __init__(self):
        self.list_ = []

    def push(self, priority, data):
        index = 0
        while index < len(self.list_) and self.list_[index][0] <= priority:
            index += 1
        self.list_.insert(index, (priority, data))

    def pop(self):
        if not self.is_empty():
            return self.list_.pop(0)[0]
        raise IndexError("Empty list")

    def is_empty(self):
        return len(self.list_) == 0

    def size(self):
        return len(self.list_)

    def show(self):
        print(self.list_)


pq = PQ()
pq.push(2, 10)
pq.push(4, 10)
pq.push(1, 10)
pq.show()
