# Python program to reverse alternative k linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head, alternate_no: int):
    rev = True
    temp = head
    prev = None

    while temp and temp.next:
        new_prev = None
        curr = temp
        if rev:
            for i in range(alternate_no):
                next_node = curr.next
                curr.next = new_prev
                new_prev = curr
                curr = next_node
            rev = False
            if not prev:
                prev = new_prev
                head = prev

            else:
                prev.next = new_prev
            temp.next = curr

        else:
            for _ in range(alternate_no):
                new_prev = curr
                curr = curr.next
            prev = new_prev
            rev = True
        temp = curr
    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Creating a sample singly linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    print_list(head)
    head = reverse_list(head, alternate_no=2)
    print_list(head)
