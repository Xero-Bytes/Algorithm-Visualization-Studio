"""
Concept 2: Binary Search
Reel: 3D Coding Concepts · 2/7
Creator: Syeda Taqdees Bukhari

Description:
Efficient search algorithm for sorted lists. Repeatedly halves
the search range by comparing the target with the middle element.

Complexity:
- Time Complexity:
  * Best Case: O(1) (Target is right at the middle)
  * Average Case: O(log n)
  * Worst Case: O(log n)
- Space Complexity:
  * Iterative: O(1)
  * Recursive: O(log n) call stack
"""

from typing import List, Optional


def binary_search(a: List[int], target: int) -> int:
    """Iterative binary search returning the index of target, or -1 if not found."""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_visual(a: List[int], target: int) -> int:
    """Detailed visual trace of binary search narrowing its range."""
    lo, hi = 0, len(a) - 1
    step = 1

    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 2: BINARY SEARCH")
    print(f"{'='*55}")
    print(f"Sorted Array : {a}")
    print(f"Target Value : {target}\n")

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = a[mid]
        print(f"Step {step}:")
        print(f"  Range: lo={lo} ({a[lo]}), mid={mid} ({mid_val}), hi={hi} ({a[hi]})")

        if mid_val == target:
            print(f"  >>> Target {target} found at index {mid}! <<<\n")
            return mid
        elif mid_val < target:
            print(f"  {mid_val} < {target} -> Discard LEFT half (lo = {mid + 1})\n")
            lo = mid + 1
        else:
            print(f"  {mid_val} > {target} -> Discard RIGHT half (hi = {mid - 1})\n")
            hi = mid - 1
        step += 1

    print(f"Target {target} not present in list.\n")
    return -1


if __name__ == "__main__":
    sample = [3, 8, 12, 17, 23, 29, 35, 42, 50]
    binary_search_visual(sample, 42)
    binary_search_visual(sample, 99)
