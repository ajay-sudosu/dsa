# Python program to reverse a linked list in groups of given size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_middle(head):
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
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
    # head.next.next.next.next.next = Node(6)
    # head.next.next.next.next.next.next = Node(7)
    print_list(head)
    head = delete_middle(head)
    print_list(head)
