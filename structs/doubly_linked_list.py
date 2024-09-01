class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DBLinkedList:

    def __init__(self):
        self.head = ListNode(0)  # Dummy node to avoid edge cases for head
        self.tail = ListNode(0)  # Dummy node to avoid edge cases for tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr != self.tail and index > 0:
            curr = curr.next
            index -=1
        if curr == self.tail:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        prev = self.head
        while prev != self.tail and index > 0:
            prev = prev.next
            index -= 1
        if prev != self.tail:
            newNode = ListNode(val)
            newNode.next = prev.next
            newNode.prev = prev
            prev.next.prev = newNode
            prev.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr != self.tail and index > 0:
            curr = curr.next
            index -= 1
        if curr != self.tail:  # If valid index
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
