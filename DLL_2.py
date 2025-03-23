class Node:
    def __init__(self, pre_ref, item, next_ref=None):
        self.item = item
        self.pre_ref = pre_ref
        self.next_ref = next_ref


class DLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def find(self, item):
        if not self.is_empty():
            temp = self.head
            while temp.next_ref is not None:
                if temp.item == item:
                    return temp
                temp = temp.next_ref
            if temp.item == item:
                return temp
            else:
                raise ValueError(f"{item} not found.")

        else:
            raise ValueError(f"{item} not found.")

    def insert_at_first(self, item):
        if not self.is_empty():
            temp = self.head
            new_node = Node(pre_ref=self.head, next_ref=temp, item=item)
            self.head = new_node
        else:
            new_node = Node(item=item, pre_ref=self.head)
            self.head = new_node

    def insert(self, item):
        if not self.is_empty():
            temp = self.head
            while temp.next_ref is not None:
                temp = temp.next_ref
            new_node = Node(pre_ref=temp, item=item)
            temp.next_ref = new_node
        else:
            self.insert_at_first(item)

    def insert_after(self, after_item, new_item):
        temp = self.find(after_item)  # node ref after which the item need to be inserted
        if temp:
            new_node = Node(pre_ref=temp, next_ref=temp.next_ref, item=new_item)
            temp.next_ref = new_node
        else:
            raise ValueError(f"{after_item} not found")

    def list(self):
        if not self.is_empty():
            temp = self.head
            while temp:
                print(temp.item, end=" ")
                temp = temp.next_ref
            print()

        else:
            return []

    def delete_first(self):
        if not self.is_empty():
            self.head = self.head.next_ref

    def delete_last(self):
        if not self.is_empty():
            temp = self.head
            if not temp.next_ref:
                self.delete_first()
            else:
                while temp.next_ref.next_ref is not None:
                    temp = temp.next_ref
                temp.next_ref = None

    def delete(self, item):
        temp = self.find(item)
        if temp:
            if not temp.pre_ref:
                self.delete_first()
            elif temp.next_ref:
                temp.pre_ref.next_ref = temp.next_ref
        elif temp and not temp.next_ref:
            self.delete_last()
        else:
            raise ValueError(f"{item} not found")

    def _iter_(self):
        return DLLIterator(self.head)


class DLLIterator:
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


s = DLL()
s.insert(10)
s.insert(20)
s.insert_after(20, 30)
s.insert(40)
s.list()
s.delete(10)
s.list()
