"""
Concept 1: Bubble Sort
Reel: 3D Coding Concepts · 1/7
Creator: Syeda Taqdees Bukhari

Description:
Repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order. Larger values
bubble up to the end of the array with each pass.

Complexity:
- Time Complexity:
  * Best Case (Already sorted): O(n)
  * Average Case: O(n^2)
  * Worst Case (Reverse sorted): O(n^2)
- Space Complexity: O(1) auxiliary (in-place)
- Stability: Stable
"""

from typing import List, Tuple


def bubble_sort(a: List[int]) -> List[int]:
    """Sorts a list in ascending order using optimized Bubble Sort."""
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        # If no swaps occurred, the list is already sorted!
        if not swapped:
            break
    return a


def bubble_sort_visual(a: List[int]) -> Tuple[List[int], int, int]:
    """Runs bubble sort while printing each step for visualization."""
    arr = list(a)
    n = len(arr)
    comparisons = 0
    swaps = 0

    print(f"\n{'='*55}")
    print(f"  3D CONCEPT 1: BUBBLE SORT")
    print(f"{'='*55}")
    print(f"Initial Array: {arr}\n")

    for p in range(n - 1):
        swapped = False
        print(f"--- Pass {p + 1} ---")
        for i in range(n - 1 - p):
            comparisons += 1
            cmp_str = f"Compare a[{i}]={arr[i]} and a[{i+1}]={arr[i+1]}"
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
                print(f"  [SWAP] {cmp_str} -> {arr}")
            else:
                print(f"  [KEEP] {cmp_str}")
        print(f"State after pass {p + 1}: {arr}\n")
        if not swapped:
            print(f"Early exit triggered! Array sorted in {p + 1} passes.")
            break

    print(f"{'='*55}")
    print(f"Sorted Array: {arr}")
    print(f"Total Comparisons: {comparisons} | Total Swaps: {swaps}")
    print(f"{'='*55}\n")
    return arr, comparisons, swaps


if __name__ == "__main__":
    sample = [2, 1, 5, 3, 6, 7]
    bubble_sort_visual(sample)
