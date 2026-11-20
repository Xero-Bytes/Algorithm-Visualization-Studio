"""
Concept 3: Stack (LIFO - Last In, First Out)
Reel: 3D Coding Concepts · 3/7
Creator: Syeda Taqdees Bukhari

Description:
A linear data structure following the LIFO principle: the newest
item pushed is always the first one to be popped out.
Common real-world uses: Function call stack, Undo/Redo operations,
Browser history back navigation, Syntax/bracket validation.

Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Space: O(n)
"""

from typing import Any, List, Optional


class Stack:
    """A clean, object-oriented Stack implementation."""

    def __init__(self) -> None:
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)
        print(f"  [PUSH] {item} -> Stack: {self._items}")

    def pop(self) -> Any:
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self._items.pop()
        print(f"  [POP]  {item} <- Stack: {self._items}")
        return item

    def peek(self) -> Optional[Any]:
        """View the top item without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"


def is_balanced_parentheses(expr: str) -> bool:
    """Real-world stack application: Verify balanced brackets."""
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 3: STACK (LIFO)")
    print(f"{'='*55}")

    # Reel demonstration sequence
    stack = []
    print("Reel code sequence:")
    stack.append(10)      # push 10
    print("  stack.append(10) ->", stack)
    stack.append(20)      # push 20
    print("  stack.append(20) ->", stack)
    stack.append(30)      # push 30
    print("  stack.append(30) ->", stack)

    top = stack.pop()     # pop 30
    print(f"  top = stack.pop() -> {top}")
    print(f"  print(top)        -> {top}")
    print(f"  print(stack[-1])  -> {stack[-1]} (peek)")

    stack.append(40)      # push 40
    print("  stack.append(40) ->", stack)

    print(f"\n--- Practical Application: Bracket Balancer ---")
    test_str = "{ [ ( 2 + 3 ) * 5 ] }"
    print(f"Checking '{test_str}': Balanced = {is_balanced_parentheses(test_str)}")
    print(f"{'='*55}\n")
