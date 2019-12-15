'''
refer to  https://www.geeksforgeeks.org/reverse-a-linked-list/
'''
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def reverse(head):
    cur = head
    pre = None
    next = None
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    head = pre
    return pre

def traverse(head):
    while head:
        print head.data
        head = head.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
traverse(head)

head = reverse(head)

traverse(head)
