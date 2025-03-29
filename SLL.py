class SLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def find(self, item):
        temp = self.head
        while temp:
            if temp.item == item:
                return temp
            temp = temp.next_ref
        return None

    def insert_at_first(self, item):
        new_node = Node(item, self.head)
        self.head = new_node

    def insert_at_last(self, item):
        new_node = Node(item)
        if not self.is_empty():
            temp = self.head
            while temp.next_ref is not None:
                temp = temp.next_ref
            temp.next_ref = new_node
        else:
            self.head = new_node

    def insert_after(self, after_item, item):
        temp = self.find(after_item)
        if temp:
            new_node = Node(item, next_ref=temp.next_ref)
            temp.next_ref = new_node
        else:
            raise ValueError(f"{after_item} not found.")

    def show(self):
        if not self.is_empty():
            temp = self.head
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next_ref
            print()
        else:
            return None

    def delete_first(self):
        if not self.is_empty():
            first_ref = self.head
            del self.head
            self.head = first_ref.next_ref
        else:
            raise ValueError('list is empty nothing to delete')

    def delete_last(self):

        if not self.is_empty():
            temp = self.head
            if temp.next_ref:
                while temp.next_ref.next_ref is not None:
                    temp = temp.next_ref
                temp.next_ref = None
            else:
                self.head = None
            del temp
        elif self.head.next_ref is None:
            self.head = None
        else:
            raise ValueError('list is empty nothing to delete')

    def delete(self, item):
        if not self.is_empty():  # if list is not empty
            item_node = self.find(item)
            if item_node:  # if item is found it is the reference of that node
                temp = self.head
                while not temp.item == item:
                    if temp.next_ref == item_node:
                        temp.next_ref = item_node.next_ref
                        break
                    temp = temp.next_ref

                else:
                    self.head = temp.next_ref
                    del temp

            else:
                raise ValueError(f"{item} not found.")
        else:
            raise ValueError('list is empty nothing to delete')

    def __iter__(self):
        return SLLIterator(self.head)


class Node:

    def __init__(self, item, next_ref=None):
        self.item = item
        self.next_ref = next_ref


class SLLIterator:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.head:
            raise StopIteration
        item = self.head.item
        self.head = self.head.next_ref
        return item


s = SLL()
s.insert_at_first(10)
s.insert_at_last(30)
s.insert_at_last(200)
s.insert_at_last(160)

print(list(s))
