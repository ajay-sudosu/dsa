class DCLL:
    def __init__(self, start=None):
        self.start = start

    def p(self):
        print("List is empty")

    def is_empty(self):
        return self.start is None

    def insert_first(self, data):
        new_node = Node(data=data)
        if not self.is_empty():
            new_node.pre_ref = self.start.pre_ref
            new_node.next_ref = self.start
            self.start.pre_ref.next_ref = new_node
            self.start.pre_ref = new_node

        else:
            new_node.pre_ref = new_node
            new_node.next_ref = new_node
        self.start = new_node

    def insert_last(self, data):
        if self.is_empty():
            self.insert_first(data)

        else:
            new_node = Node(data=data, pre_ref=self.start.pre_ref, next_ref=self.start)
            new_node.pre_ref.next_ref = new_node
            self.start.pre_ref = new_node

    def insert_after(self, after, data):
        if self.is_empty():
            self.p()

        else:
            new_node = Node(data=data)

            if self.start.next_ref == self.start.pre_ref and self.start.data == after:  # insert after only one node
                new_node.next_ref = self.start.next_ref
                new_node.pre_ref = self.start
                self.start.next_ref = new_node

            else:
                # process if there are at least more than one node
                temp = self.start
                while temp.next_ref != self.start:
                    if temp.data == after:
                        new_node.next_ref = temp.next_ref
                        new_node.pre_ref = temp
                        temp.next_ref = new_node
                        break
                    temp = temp.next_ref
                else:
                    # condition if data to be inserted after last item in the list
                    if temp.data == after:
                        self.insert_last(data)
                    else:
                        print(f"{after} not found")

    def delete_first(self):
        if self.is_empty():
            self.p()

        else:
            if self.start.pre_ref == self.start:
                self.start = None
            else:
                self.start.next_ref.pre_ref = self.start.pre_ref
                self.start.pre_ref.next_ref = self.start.next_ref
                self.start = self.start.next_ref

    def delete_last(self):
        if self.is_empty():
            self.p()

        else:
            if self.start.pre_ref == self.start:
                self.delete_first()

            else:
                self.start.pre_ref.pre_ref.next_ref = self.start
                self.start.pre_ref = self.start.pre_ref.pre_ref

    def delete(self, data):
        if self.is_empty():
            self.p()

        else:
            if self.start.data == data:
                self.delete_first()

            else:
                temp = self.start.next_ref
                while temp != self.start:
                    if temp.data == data:
                        temp.pre_ref.next_ref = temp.next_ref
                        temp.next_ref.pre_ref = temp.pre_ref
                        break
                    temp = temp.next_ref

                else:
                    print(f"{data} not found")

    def show(self):
        if self.is_empty():
            self.p()

        else:
            temp = self.start
            while temp != self.start.pre_ref:
                print(temp.data, end=" ")
                temp = temp.next_ref
            print(temp.data, end=" ")
            print()


class Node:
    def __init__(self, data, pre_ref=None, next_ref=None):
        self.data = data
        self.pre_ref = pre_ref
        self.next_ref = next_ref


dcll = DCLL()
dcll.insert_last(3)
dcll.insert_last(4)
dcll.insert_last(5)
dcll.insert_last(6)
# dcll.insert_after(after=3, data=20)
# dcll.insert_after(after=20, data=40)
dcll.show()
dcll.delete(data=6)
dcll.show()

