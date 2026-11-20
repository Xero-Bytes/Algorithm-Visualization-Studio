"""
Concept 4: Queue (FIFO - First In, First Out)
Reel: 3D Coding Concepts · 4/7
Creator: Syeda Taqdees Bukhari

Description:
A linear data structure where elements are added at the rear (enqueue)
and removed from the front (dequeue). First arrived is first served.
Common real-world uses: Printer spools, CPU task scheduling,
Breadth-First Search (BFS) frontier, message brokers (Kafka/RabbitMQ).

Complexity:
- Enqueue (append): O(1)
- Dequeue (popleft): O(1) with collections.deque
- Space: O(n)
"""

from collections import deque
from typing import Any, Optional


class Queue:
    """Thread-safe, double-ended queue wrapper with O(1) FIFO operations."""

    def __init__(self) -> None:
        self._items = deque()

    def enqueue(self, item: Any) -> None:
        """Add item to the rear of the queue."""
        self._items.append(item)
        print(f"  [ENQUEUE] '{item}' -> Queue: {list(self._items)}")

    def dequeue(self) -> Any:
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items.popleft()
        print(f"  [DEQUEUE] '{item}' <- Queue: {list(self._items)}")
        return item

    def peek(self) -> Optional[Any]:
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 4: QUEUE (FIFO)")
    print(f"{'='*55}")

    # Exact reel code execution
    print("Reel code sequence:")
    q = deque()
    q.append("A")      # enqueue A
    print("  q.append('A')   ->", list(q))
    q.append("B")      # enqueue B
    print("  q.append('B')   ->", list(q))
    q.append("C")      # enqueue C
    print("  q.append('C')   ->", list(q))

    x = q.popleft()    # dequeue A
    print(f"  x = q.popleft() -> {x}")
    print(f"  print(x)        -> {x} (first in, first out)")

    q.append("D")      # enqueue D
    print("  q.append('D')   ->", list(q))

    y = q.popleft()    # dequeue B
    print(f"  q.popleft()     -> {y} leaves next")
    print(f"  Final Queue     -> {list(q)}")
    print(f"{'='*55}\n")
