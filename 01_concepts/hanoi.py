"""
Concept 6: Tower of Hanoi (Recursion)
Reel: 3D Coding Concepts · 6/7
Creator: Syeda Taqdees Bukhari

Description:
Classic mathematical puzzle demonstrating recursion. The goal is to
move n discs from source peg to destination peg using an auxiliary peg,
subject to:
1. Only one disc can be moved at a time.
2. A larger disc can never be placed on top of a smaller disc.

Recurrence Relation:
T(n) = 2 * T(n-1) + 1
Total Moves = 2^n - 1

Complexity:
- Time: O(2^n)
- Space: O(n) (Maximum call stack depth)
"""

from typing import List


def hanoi(n: int, src: str, dst: str, aux: str, moves_record: List[str] = None) -> None:
    """Exact recursive Tower of Hanoi function from the reel."""
    if n == 0:
        return
    # Step 1: Move top n-1 discs from src to aux using dst
    hanoi(n - 1, src, aux, dst, moves_record)

    # Step 2: Move the largest disc from src to dst
    msg = f"move disc {n}: {src} -> {dst}"
    print(f"  {msg}")
    if moves_record is not None:
        moves_record.append(msg)

    # Step 3: Move n-1 discs from aux to dst using src
    hanoi(n - 1, aux, dst, src, moves_record)


if __name__ == "__main__":
    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 6: TOWER OF HANOI")
    print(f"{'='*55}")

    DISCS = 3
    expected_moves = (2 ** DISCS) - 1
    print(f"Solving Tower of Hanoi for {DISCS} discs:")
    print(f"Formula: 2^{DISCS} - 1 = {expected_moves} minimum moves required\n")

    records = []
    hanoi(DISCS, "A", "C", "B", records)

    print(f"\nTotal moves executed: {len(records)} / {expected_moves}")
    print(f"{'='*55}\n")
