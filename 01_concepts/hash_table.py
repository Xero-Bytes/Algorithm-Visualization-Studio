"""
Concept 7: Hash Table (Separate Chaining)
Reel: 3D Coding Concepts · 7/7
Creator: Syeda Taqdees Bukhari

Description:
A data structure that maps keys to values using a hash function.
The hash function computes an integer bucket index from the key.
Collisions are resolved via separate chaining (lists in each bucket).

Complexity:
- Search: O(1) average, O(n) worst case
- Insertion: O(1)
- Deletion: O(1) average
- Space: O(n)
"""

from typing import Any, List, Optional, Tuple


def h(key: str, size: int = 5) -> int:
    """Exact polynomial ASCII sum hash function from the reel."""
    return sum(map(ord, str(key))) % size


class HashTable:
    """Full Hash Table implementation with separate chaining."""

    def __init__(self, size: int = 5) -> None:
        self.size = size
        self.table: List[List[Tuple[str, Any]]] = [[] for _ in range(size)]

    def set(self, key: str, value: Any) -> None:
        idx = h(key, self.size)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str) -> Optional[Any]:
        idx = h(key, self.size)
        bucket = self.table[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def display(self) -> None:
        print(f"Hash Table State (size={self.size}):")
        for i, bucket in enumerate(self.table):
            items = " -> ".join([f"({k}: {v})" for k, v in bucket]) or "empty"
            print(f"  Bucket [{i}]: {items}")


if __name__ == "__main__":
    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 7: HASH TABLE")
    print(f"{'='*55}")

    # Exact reel code execution
    print("Reel code sequence:")
    table = [[] for _ in range(5)]
    keys = ["cat", "dog", "sun", "bee"]

    for key in keys:
        i = h(key, size=5)
        raw_sum = sum(map(ord, key))
        table[i].append(key)
        print(f"  key='{key}' -> sum={raw_sum} -> h('{key}') = {raw_sum} % 5 = {i} -> Bucket {i}")

    print(f"\nFinal Buckets:")
    for idx, b in enumerate(table):
        print(f"  Bucket {idx}: {b}")
    print(f"{'='*55}\n")
