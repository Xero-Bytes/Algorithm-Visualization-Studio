"""
Concept 5: Singly Linked List
Reel: 3D Coding Concepts · 5/7
Creator: Syeda Taqdees Bukhari

Description:
A collection of nodes linked together by pointers. Each node contains
a value and a pointer (reference) to the next node. Unlike arrays,
elements are not stored in contiguous memory locations.

Complexity:
- Insert at Head: O(1)
- Access / Search: O(n)
- Delete Node: O(n) (or O(1) if pointer is given)
- Space: O(n) (with extra memory for pointer links)
"""

from typing import Any, Optional


class Node:
    """Single node in a linked list."""

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next: Optional["Node"] = None

    def __repr__(self) -> str:
        return f"Node({self.val})"


class LinkedList:
    """Full singly linked list implementation."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, val: Any) -> None:
        """Appends value at the end."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, val: Any) -> None:
        """Inserts value at the head in O(1) time."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def traverse(self) -> None:
        """Walks through the linked list following pointers."""
        cur = self.head
        chain = []
        while cur:
            chain.append(str(cur.val))
            cur = cur.next
        chain.append("None")
        print(" -> ".join(chain))

    def reverse(self) -> None:
        """Reverses the linked list in-place."""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


if __name__ == "__main__":
    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 5: LINKED LIST")
    print(f"{'='*55}")

    # Exact reel code execution
    print("Reel code sequence:")
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    cur = head
    while cur:
        print(f"  cur = {cur.val} -> following pointer to {cur.next}")
        cur = cur.next

    print(f"\n--- OOP LinkedList Extended Demo ---")
    ll = LinkedList()
    for val in [10, 20, 30, 40]:
        ll.append(val)
    print("Original List:")
    ll.traverse()

    print("Prepend 5:")
    ll.prepend(5)
    ll.traverse()

    print("Reversed List:")
    ll.reverse()
    ll.traverse()
    print(f"{'='*55}\n")
