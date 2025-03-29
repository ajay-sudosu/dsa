def reverse(head):
    temp = head
    prev = None
    while temp.next:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
        head = temp
    temp.next = prev
    return head


def remove_leading_zeros(head):
    while head and head.data == 0:
        head = head.next
    return head


def add_num(head1, head2):
    list1 = remove_leading_zeros(head1)
    list2 = remove_leading_zeros(head2)

    list1 = reverse(head1)
    list2 = reverse(head2)

    carry = 0
    start = None
    temp = None

    while list1 or list2 or carry != 0:
        sum = carry
        if list1:
            sum += list1.data
            list1 = list1.next

        if list2:
            sum += list2.data
            list2 = list2.next


        new_node = Node(sum % 10)
        carry = sum // 10

        if not start:
            start = new_node
            temp = new_node
        else:
            temp.next = new_node
            temp = temp.next

    return reverse(start)


def show(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


if __name__ == "__main__":
    class Node:
        def __init__(self, val):
            self.data = val
            self.next = None

    num1 = Node(0)
    num1.next = Node(2)
    num1.next.next = Node(3)

    num2 = Node(9)
    num2.next = Node(9)
    num2.next.next = Node(9)
    res = add_num(head1=num1, head2=num2)
    show(res)
