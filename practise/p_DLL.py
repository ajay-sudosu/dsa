class Node:
    def __init__(self, data, pre_ref=None, next_ref=None):
        self.next_ref = next_ref
        self.prev_ref = pre_ref
        self.data = data


class DLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_first(self, data):
        temp = self.head
        new_node = Node(data)
        self.head = new_node
        new_node.next_ref = temp

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data)
        else:
            temp = self.head
            while temp.next_ref is not None:
                temp = temp.next_ref
            new_node = Node(data=data, pre_ref=temp)
            temp.next_ref = new_node

    def insert_after(self, insert_after, data):
        found = self.find(data=insert_after)
        if found:
            found.next_ref = Node(data=data, pre_ref=found, next_ref=found.next_ref)
        else:
            print(f"{insert_after} not found")

    def find(self, data):
        if self.is_empty():
            print("List is empty")

        else:
            temp = self.head
            while temp:
                if temp.data == data:
                    return temp
                temp = temp.next_ref
            return None

    def list_(self):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.head
            while temp.next_ref is not None:
                print(temp.data, end=" ")
                temp = temp.next_ref
            print(temp.data)

    def delete_first(self):
        if not self.is_empty():
            self.head = self.head.next_ref
        else:
            print("List is empty.")

    def delete_last(self):
        if not self.is_empty():
            temp = self.head

            if not temp.next_ref:
                self.delete_first()
            else:
                while temp.next_ref.next_ref is not None:
                    temp = temp.next_ref

                temp.next_ref = None
        else:
            print("List is empty.")

    def delete(self, data):
        found = self.find(data)
        if found:
            if not found.prev_ref:
                self.delete_first()
            elif not found.next_ref:
                self.delete_last()
            else:
                found.prev_ref.next_ref = found.next_ref

        else:
            print(f"{data} not found")


dll = DLL()
dll.insert_first(20)
dll.insert_first(10)
dll.insert_last(50)
dll.insert_after(50, 60)
dll.list_()
dll.delete(50)
dll.list_()
