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


def rev_alternate(head, k):
    rev = True

    temp = head
    star_prev = None
    while temp and temp.next:
        new_prev = None
        curr = temp
        if rev:
            for _ in range(1, k+1):
                next_node = curr.next
                curr.next = new_prev
                new_prev = curr
                curr = next_node

            if not star_prev:
                star_prev = new_prev
                head = star_prev
            else:
                star_prev.next = new_prev
            temp.next = curr

            rev = False
        else:
            for _ in range(1, k+1):
                if not curr:
                    break
                new_prev = curr
                curr = curr.next
            rev = True
        star_prev = new_prev
        temp = curr

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
    head = rev_alternate(head, k=2)
    print("Modified list: ", end="")
    show(head)
