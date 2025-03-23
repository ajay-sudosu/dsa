class Node:

    def __init__(self, item=None, next_ref=None):
        self.item = item
        self.next_ref = next_ref


class CLL:
    def __init__(self, last_ref=None):
        self.last_ref = last_ref

    def is_empty(self):
        return self.last_ref is None

    def insert_at_start(self, item):
        if self.is_empty():
            new_node = Node(item=item)
            new_node.next_ref = new_node
            self.last_ref = new_node

        else:
            # reference of the first node is being transferred to new node's next
            new_node = Node(item=item, next_ref=self.last_ref.next_ref)
            self.last_ref.next_ref = new_node

    def insert_at_last(self, item):
        new_node = Node(item=item)
        if self.is_empty():
            self.insert_at_start(item=item)
        else:
            new_node = Node(item=item)
            new_node.next_ref = self.last_ref.next_ref
            self.last_ref.next_ref = new_node
            self.last_ref = new_node

    def search(self, item):
        if self.is_empty():
            raise ValueError(f"{item} not found.")
        temp = self.last_ref.next_ref
        while temp != self.last_ref:
            if temp.item == item:
                return temp
            temp = temp.next_ref
        if temp.item == item:
            return temp
        raise ValueError(f"{item} not found.")

    def insert_after(self, insert_after, item):
        if self.is_empty():
            raise ValueError(f"{insert_after} not found.")

        after_item_ref = self.search(item=insert_after)

        new_node = Node(item=item, next_ref=after_item_ref.next_ref)
        after_item_ref.next_ref = new_node

        if after_item_ref == self.last_ref:
            self.last_ref = new_node

    def list(self):
        if not self.is_empty():
            temp = self.last_ref.next_ref
            while temp != self.last_ref:
                print(temp.item, end=" ")
                temp = temp.next_ref
            print(temp.item)
        else:
            raise ValueError("List is empty.")

    def delete_first(self):
        if self.is_empty():
            raise ValueError("List is empty nothing to delete.")
        if self.last_ref.next_ref == self.last_ref:
            self.last_ref = None
        else:
            self.last_ref.next_ref = self.last_ref.next_ref.next_ref

    def delete_last(self):
        if not self.is_empty():
            if self.last_ref.next_ref == self.last_ref:
                self.last_ref = None

            else:
                temp = self.last_ref.next_ref
                while temp.next_ref != self.last_ref:
                    temp = temp.next_ref
                temp.next_ref = self.last_ref.next_ref
                self.last_ref = temp

        else:
            raise ValueError("Nothing to delete, list is empty.")

    def delete(self, item):
        if not self.is_empty():
            if self.last_ref == self.last_ref.next_ref:
                if self.last_ref.item == item:
                    self.delete_first()
            else:
                temp = self.last_ref.next_ref
                if temp.item == item:
                    self.delete_first()
                while temp != self.last_ref:
                    if temp.next_ref == self.last_ref:
                        if temp.next_ref.item == item:
                            self.delete_last()
                        break
                    if temp.next_ref.item == item:
                        temp.next_ref = temp.next_ref.next_ref
                        break
                    temp = temp.next_ref

        else:
            raise ValueError("Nothing to delete, list is empty.")


cll = CLL()
cll.insert_at_start(50)
cll.insert_at_start(40)
cll.insert_at_start(30)
cll.list()
cll.delete(50)
cll.list()
