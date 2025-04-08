class Node:
    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


def show(head):
    temp = head

    while temp.next_ref is not None:
        print(temp.data, end=" ")
        temp = temp.next_ref
    print(temp.data, end=" ")
    print()


def rev_sublist(head, k):
    temp = head
    tail = None
    new_head = None

    while temp:
        grp_head = temp
        prev = None
        count = 0
        while temp and count < k:
            next_ref = temp.next_ref
            temp.next_ref = prev
            prev = temp
            temp = next_ref
            count += 1

        if not new_head:
            new_head = prev

        if not tail:
            tail = grp_head
        else:
            tail.next_ref = prev
            tail = grp_head
    return new_head


if __name__ == "__main__":
    # Creating a sample singly linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next_ref = Node(2)
    head.next_ref.next_ref = Node(3)
    head.next_ref.next_ref.next_ref = Node(4)
    head.next_ref.next_ref.next_ref.next_ref = Node(5)
    show(head)
    res = rev_sublist(head, 2)
    show(res)
