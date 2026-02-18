"""
Design a Singly Linked List class.
Your LinkedList class should support the following operations:
-LinkedList() will initialize an empty linked list.
-int get(int i) will return the value of the ith node (0-indexed). If the index is
out of bounds, return -1.
-void insertHead(int val) will insert a node with val at the head of the list.
-void insertTail(int val) will insert a node with val at the tail of the list.
-bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds,
return false, otherwise return true.
-int[] getValues() return an array of all the values in the linked list, ordered from
head to tail.

Sample Input/Output:
Input:
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]

"""


# Singly Linked List Node
class ListNode:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


# Implementation for Singly Linked List
class LinkedList:

    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds or list is empty

    def insert_head(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # If list was empty before insertion
        if not new_node.next:
            self.tail = new_node

    def insert_tail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def get_values(self) -> list[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


def main():
    # ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
    # [null, null, null, true, [0, 2]]
    linked_list = LinkedList()
    print(linked_list.insert_head(1))
    print(linked_list.insert_tail(2))
    print(linked_list.insert_head(0))
    print(linked_list.remove(1))
    print(linked_list.get_values())


if __name__ == '__main__':
    main()
