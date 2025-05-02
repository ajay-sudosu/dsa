from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def rev(head):
#     prev = None
#     temp = head
#
#     while temp.next:
#         next_node = temp.next
#         temp.next = prev
#         prev = temp
#         temp = next_node
#     temp.next = prev
#     return temp


# class Solution:
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # l1 = rev(l1)
    # l2 = rev(l2)

    carry = 0
    start = None
    temp = None


    while l1 or l2 or carry != 0:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        dummy_node = ListNode(sum % 10)
        if not start:
            start = dummy_node
            temp = dummy_node

        else:
            temp.next = dummy_node
            temp = temp.next

    # result = rev(start)
    return start


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

num1 = ListNode(2)
num1.next = ListNode(4)
num1.next.next = ListNode(9)


num2 = ListNode(5)
num2.next = ListNode(6)
num2.next.next = ListNode(4)
num2.next.next.next = ListNode(9)

result = addTwoNumbers(l1=num1, l2=num2)
print_list(result)