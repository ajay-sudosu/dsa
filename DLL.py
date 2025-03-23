class DLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_at_first(self, item):
        temp = self.head
        new_node = Node(item)
        self.head = new_node
        new_node.next_ref = temp

    def insert_at_last(self, item):
        temp = self.head
        if not self.is_empty():
            while temp.next_ref is not None:
                temp = temp.next_ref
            new_node = Node(pre_ref=temp, item=item)
            temp.next_ref = new_node
        else:
            self.insert_at_first(item)

    def find(self, item):
        if self.is_empty():
            raise ValueError(f"{item} not found.")
        else:
            temp = self.head
            while temp:
                if item == temp.item:
                    return temp
                temp = temp.next_ref
            raise ValueError(f"{item} not found.")

    def insert_after(self, item, new_item):
        if self.is_empty():
            raise ValueError(f"{item} not found.")
        else:
            temp = self.find(item)
            while temp.next_ref is not None:
                temp.next_ref = Node(new_item, pre_ref=temp, next_ref=temp.next_ref)
                break
            else:
                temp.next_ref = Node(pre_ref=temp, item=new_item)
        # else:
        #     self.insert_at_first(item)

    def list(self):
        if not self.is_empty():
            temp = self.head
            while temp.next_ref is not None:
                print(temp.item)
                temp = temp.next_ref
            print(temp.item)
        return


class Node:
    def __init__(self, item, pre_ref=None, next_ref=None):
        self.item = item
        self.pre_ref = pre_ref
        self.next_ref = next_ref


s = DLL()
s.insert_at_first(70)
s.insert_at_first(50)
s.insert_after(50, 40)
s.list()
