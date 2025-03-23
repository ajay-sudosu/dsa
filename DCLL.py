class Node:
    def __init__(self, data, prev_ref=None, next_ref=None):
        self.data = data
        self.prev_ref = prev_ref
        self.next_ref = next_ref


class DCLL:

    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if not self.start:
            return True
        return False

    def insert_first(self, data):
        new_node = Node(data=data)
        if self.is_empty():
            new_node.next_ref = new_node
            new_node.prev_ref = new_node
        else:
            new_node.next_ref = self.start
            new_node.prev_ref = self.start.prev_ref
            self.start.prev_ref.next_ref = new_node
            self.start.prev_ref = new_node

        self.start = new_node

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data=data)
        else:
            new_node = Node(data=data)
            new_node.next_ref = self.start
            new_node.prev_ref = self.start.prev_ref
            new_node.prev_ref.next_ref = new_node
            self.start.prev_ref = new_node

    def insert_after(self, after, data):
        found = self.search(data=after)
        if found is not None:
            new_node = Node(data=data)
            new_node.next_ref = found.next_ref
            new_node.prev_ref = found
            found.next_ref.prev_ref = new_node
            found.next_ref = new_node

    def search(self, data):
        if self.is_empty():
            print("The list is empty")
        else:
            temp = self.start
            while temp != self.start.prev_ref:
                if temp.data == data:
                    return temp
                temp = temp.next_ref
            else:
                if temp.data == data:
                    return temp
                else:
                    print(f"{data} not found")

    def delete_first(self):
        if self.is_empty():
            print("This is empty list")
        else:
            if self.start.prev_ref == self.start:
                self.start = None
            else:
                self.start.prev_ref.next_ref = self.start.next_ref
                self.start.next_ref.prev_ref = self.start.prev_ref
                self.start = self.start.next_ref

    def delete_last(self):
        if self.is_empty():
            print("List is empty")
        else:
            if self.start.prev_ref == self.start:
                self.delete_first()

            else:
                self.start.prev_ref = self.start.prev_ref.prev_ref
                self.start.prev_ref.prev_ref.next_ref = self.start

    def delete(self, data):
        if self.is_empty():
            print("The list is empty")

        else:
            if self.start.data == data:
                self.delete_first()

            else:
                temp = self.start.next_ref
                while temp != self.start:
                    if temp.data == data:
                        temp.next_ref.prev_ref = temp.prev_ref
                        temp.prev_ref.next_ref = temp.next_ref
                    temp = temp.next_ref

    def show(self):
        if not self.is_empty():
            first_node = self.start
            while first_node != self.start.prev_ref:
                print(first_node.data, end=" ")
                first_node = first_node.next_ref
            print(first_node.data, end=" \n")

        else:
            print("List is empty.")


dcll = DCLL()
dcll.insert_first(40)
dcll.insert_last(50)
dcll.insert_last(60)
dcll.insert_last(70)
# dcll.insert_after(50, 41)
dcll.show()
dcll.delete(60)
dcll.show()
