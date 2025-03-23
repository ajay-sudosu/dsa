class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CLL:
    MESSAGE = "List is empty"

    def __init__(self, tail=None):
        self.tail = tail

    def is_empty(self):
        return self.tail is None

    def insert_first(self, data):
        if self.is_empty():
            new_node = Node(data)
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node = Node(data, self.tail.next)
            self.tail.next = new_node

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data)
        else:
            new_node = Node(data, self.tail.next)
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, after, data):
        if self.is_empty():
            print(self.MESSAGE, f"{after} not found")
        else:
            temp = self.tail.next
            new_node = Node(data=data)
            while temp.next != self.tail.next:
                if temp.data == after:
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                temp = temp.next
            else:
                if temp.data == after:
                    self.insert_last(data=data)
                else:
                    print(f"{after} not found")

    def delete_first(self):
        if self.is_empty():
            print(self.MESSAGE)
        else:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next

    def delete_last(self):
        if self.is_empty():
            print(self.MESSAGE)
        else:
            temp = self.tail.next
            if temp == self.tail:
                self.delete_first()
            else:
                while temp.next.next != self.tail.next:
                    temp = temp.next
                temp.next = self.tail.next
                self.tail = temp

    def delete(self, data):
        if self.is_empty():
            print(self.MESSAGE)
        else:
            temp = self.tail.next
            if temp.data == data:
                self.delete_first()
            else:
                while temp.next.next != self.tail.next:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                else:
                    if temp.next.data == data:
                        self.delete_last()
                    else:
                        print(f"{data} not found")

    def show(self):
        if self.is_empty():
            print(self.MESSAGE)
        else:
            temp = self.tail.next
            while temp != self.tail:
                print(temp.data, end=" ")
                temp = temp.next
            print(temp.data)


# Example usage
cll = CLL()
cll.insert_last(10)
cll.insert_last(20)
cll.insert_last(200)
# cll.insert(data=30, after=10)
cll.show()
# cll.delete(20)
# cll.show()
