class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

c = ListNode(data=6, next_node=None)
b = ListNode(data=4, next_node=c)
a = ListNode(data=2, next_node=b)

z = ListNode(data=5, next_node=None)
y = ListNode(data=3, next_node=z)
x = ListNode(data=1, next_node=y)


def print_data(start):
    head = start
    while True:
        print(head.data)
        if not head.next:
            break
        head = head.next


def sort_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2

    print_data(dummy_head.next)

sort_lists(a, x)
