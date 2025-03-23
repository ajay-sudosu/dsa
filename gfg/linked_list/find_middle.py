class SLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_first(self, data):
        new_node = Node(data=data, next_ref=self.head)
        self.head = new_node

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data=data)
        else:
            new_node = Node(data=data)
            temp = self.head
            while temp.next_ref is not None:
                temp = temp.next_ref
            temp.next_ref = new_node

    def search(self, data):
        if self.is_empty():
            raise ValueError(f"{data} not found.")
        temp = self.head
        while temp.next_ref is not None:
            if temp.data == data:
                return temp
            temp = temp.next_ref
        if temp.data == data:
            return temp
        else:
            raise ValueError(f"{data} not found.")

    def insert_after(self, after, data):
        if self.is_empty():
            print("No such element found, list is empty.")

        ele_ref = self.search(data=after)
        new_node = Node(data=data, next_ref=ele_ref.next_ref)
        ele_ref.next_ref = new_node

    def list(self):
        if self.is_empty():
            print("List is empty.")
        else:
            temp = self.head

            while temp.next_ref is not None:
                print(temp.data, end=" ")
                temp = temp.next_ref
            print(temp.data, end=" ")
            print()

    def delete_first(self):
        if not self.is_empty():
            self.head = self.head.next_ref

        else:
            print("List is empty nothing to delete.")

    def delete_last(self):
        if self.is_empty():
            print("List is empty nothing to delete.")

        elif self.head.next_ref is None:
            self.delete_first()

        else:
            temp = self.head
            while temp.next_ref.next_ref is not None:
                temp = temp.next_ref
            temp.next_ref = None

    def delete(self, data):
        if self.is_empty():
            print("List is empty nothing to delete.")

        elif not self.head.next_ref:  # condition to check only single node if only one node delete it
            self.delete_first()

        else:  # condition to have more than one node in the linked list
            found_ = self.search(data=data)
            temp = self.head
            if temp.data == found_.data:
                self.delete_first()

            else:
                while temp.next_ref == found_:
                    temp.next_ref = found_.next_ref

                temp = temp.next_ref

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next_ref:
            slow = slow.next_ref
            fast = fast.next_ref.next_ref

        return slow.data


class Node:

    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


sll = SLL()

sll.insert_last(1)
sll.insert_last(2)
sll.insert_last(3)
sll.insert_last(4)
sll.insert_last(5)
sll.insert_last(6)
sll.list()
print(sll.find_middle())
