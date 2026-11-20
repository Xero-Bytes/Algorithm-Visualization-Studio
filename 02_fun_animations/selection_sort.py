"""
Fun Reel 1: Selection Sort (Penguin Animation)
Creator: Syeda Taqdees Bukhari

Description:
Divides the list into sorted and unsorted subarrays. Repeatedly
finds the minimum element from the unsorted subarray and swaps
it into its final position at the beginning of the unsorted part.

Complexity:
- Time: O(n^2) for all cases (always makes n*(n-1)/2 comparisons)
- Space: O(1) auxiliary
- Swaps: O(n) minimum swap count among basic sorting algorithms
"""

from typing import List


def selection_sort(a: List[int]) -> List[int]:
    """Exact selection sort from the reel."""
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def selection_sort_visual(a: List[int]) -> List[int]:
    """Visual trace of Selection Sort with min-pointer tracking."""
    arr = list(a)
    n = len(arr)

    print(f"\n{'='*55}")
    print(f"  FUN REEL 1: SELECTION SORT (PENGUIN THEME)")
    print(f"{'='*55}")
    print(f"Initial Array: {arr}\n")

    for i in range(n - 1):
        m = i
        print(f"Pass {i + 1}: Find smallest from position {i}")
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
                print(f"  -> Found smaller: arr[{j}]={arr[j]} (new min)")
        arr[i], arr[m] = arr[m], arr[i]
        print(f"  Swap arr[{i}] and min arr[{m}] -> {arr}\n")

    print(f"{'='*55}")
    print(f"Sorted Array: {arr}")
    print(f"{'='*55}\n")
    return arr


if __name__ == "__main__":
    sample = [6, 4, 5, 3, 2, 1]
    selection_sort_visual(sample)
