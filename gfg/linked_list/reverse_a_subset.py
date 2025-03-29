"""
Python3 program to reverse a linked list from position m to position n
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def show(head):
    temp = head

    while temp.next is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print(temp.data, end=" ")
    print()


def reverse_subset(head, start, end):
    prev = None
    temp = head
    i = 1
    while i < start:
        prev = temp
        temp = temp.next
        i += 1

    prev_again = None
    current_head = temp
    for _ in range(start, end+1):
        next_node = current_head.next
        current_head.next = prev_again
        prev_again = current_head
        current_head = next_node
    if not prev:
        head = prev_again
    else:
        prev.next = prev_again

    temp.next = current_head
    return head


if __name__ == "__main__":
    # Initialize linked list:
    # 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    head.next.next.next.next.next.next = Node(70)
    print("Original list: ", end="")
    show(head)
    head = reverse_subset(head, 1, 6)
    print("Modified list: ", end="")
    show(head)
