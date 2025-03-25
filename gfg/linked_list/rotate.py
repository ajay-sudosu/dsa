"""
Rotate the list by k elements
"""


class SLL:
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_first(self, data):
        new_node = Node(data=data, next_ref=self.head)
        self.head = new_node
        self.count += 1

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data=data)
        else:
            new_node = Node(data=data)
            temp = self.head
            while temp.next_ref is not None:
                temp = temp.next_ref
            temp.next_ref = new_node
            self.count += 1

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
        self.count += 1


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
            self.count -= 1

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
            self.count -= 1

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
                self.count -= 1

    def rotate(self, rotate_by: int):
        first_node = temp = self.head
        rotate_node = None
        for i in range(rotate_by):
            self.head = temp.next_ref
            temp = temp.next_ref
            rotate_node = temp
        else:
            curr_node = temp
            while curr_node.next_ref:
                curr_node = curr_node.next_ref
            curr_node.next_ref = first_node

        while first_node.next_ref != rotate_node:
            print(first_node.data, end=" ")
            first_node = first_node.next_ref
        print(first_node.data, end=" ")

    def o_rotate(self, rotate_by: int):
        """
        Optimized rotating with less loop
        """
        temp = self.head
        while temp.next_ref:  # loop to reach the last node
            temp = temp.next_ref

        temp.next_ref = self.head  # joining the next_ref of last node to first node
        new_head = None
        curr = self.head
        for i in range(rotate_by - 1):  # traversing till the kth -1 node so that next node could be the head
            curr = curr.next_ref

        new_head = curr.next_ref  # making the new head after rotating
        curr.next_ref = None  # making the current node's next_ref as None

        while new_head.next_ref:  # looping to print the node data
            print(new_head.data, end=" ")
            new_head = new_head.next_ref
        print(new_head.data, end=" ")


class Node:

    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


sll = SLL()

sll.insert_first(data=20)
sll.insert_last(data=30)
sll.insert_last(data=40)
sll.insert_last(data=50)
sll.insert_after(after=20, data=25)
sll.show()
# sll.rotate(rotate_by=4)
sll.o_rotate(rotate_by=2)
