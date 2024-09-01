class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = ListNode(0)  # Dummy node to avoid edge cases for head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr is not None and index > 0:
            curr = curr.next
            index -= 1
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next
            if curr is None:
                return None


"""
from structs.linked_list import LinkedList

linked_list = LinkedList()

linked_list.addAtHead(4)
linked_list.addAtHead(3)
linked_list.addAtHead(7)
linked_list.traverse()
"""