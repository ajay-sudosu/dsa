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

    def show(self):
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

    def reverse(self):
        if self.is_empty():
            return "Empty list"

        prev_ref = None
        temp = self.head

        while temp.next_ref:
            next_node = temp.next_ref  # saving the next node ref
            temp.next_ref = prev_ref  # feeding the prev_ref to current node
            prev_ref = temp  # updated the prev ref with the current node ref

            temp = next_node  # reassigning temp with the next node as saved before
            self.head = temp  # updating the head to next node with the temp (which is a next_node now)
        temp.next_ref = prev_ref  # last node condition to change the prev_ref


class Node:

    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


sll = SLL()

sll.insert_first(1)
sll.insert_last(2)
sll.insert_last(3)
sll.insert_last(4)
sll.show()
sll.reverse()
sll.show()
