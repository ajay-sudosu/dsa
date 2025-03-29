def intersection_node(greater_head, short_head, diff):

    for i in range(diff):
        greater_head = greater_head.next_ref

    while greater_head != short_head:
        greater_head = greater_head.next_ref
        short_head = short_head.next_ref
    return short_head


def get_count(head):
    count = 0
    while head:
        count += 1
        head = head.next_ref
    return count


class Node:

    def __init__(self, data, next_ref=None):
        self.data = data
        self.next_ref = next_ref


if __name__ == "__main__":

    # creation of first list: 10 -> 15 -> 30
    head1 = Node(10)
    head1.next_ref = Node(15)
    head1.next_ref.next_ref = Node(30)

    # creation of second list: 3 -> 6 -> 9 -> 15 -> 30
    head2 = Node(3)
    head2.next_ref = Node(6)
    head2.next_ref.next_ref = Node(9)

    # 15 is the intersection point
    head2.next_ref.next_ref.next_ref = head1.next_ref

    l1_count = get_count(head1)
    l2_count = get_count(head2)
    diff = abs(l1_count - l2_count)
    if l1_count > l2_count:  # if list one is bigger then pass the first parameter as large list ref
        result = intersection_node(head1, head2, diff=diff)
    else:
        result = intersection_node(head2, head1, diff=diff)  # if list second is bigger then pass the first parameter as large list ref

    print(result.data)