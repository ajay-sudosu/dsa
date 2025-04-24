# Python program to reverse a linked list in groups of given size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head, k: int):
    temp = head
    tail = None

    while temp and temp.next:
        current_tail = temp
        current_head = None
        curr = temp
        for i in range(k):
            next_node = curr.next
            curr.next = current_head
            current_head = curr
            curr = next_node
        if not tail:
            tail = temp
            head = current_head

        else:
            tail.next = current_head
            tail = current_tail
        temp = curr
    tail.next = temp
    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Creating a sample singly linked list:
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    # head.next.next.next.next.next.next = Node(7)
    print_list(head)
    head = reverse_list(head, k=2)
    print_list(head)
