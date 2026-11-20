"""
Fun Reel 3: Dynamic Programming (Penguin Climbing Stairs)
Creator: Syeda Taqdees Bukhari

Description:
A penguin climbing stairs where each jump can be 1 or 2 steps.
Solves the problem using dynamic programming (overlapping subproblems
and optimal substructure) by tabulating solutions:
dp[i] = dp[i-1] + dp[i-2]

Complexity:
- Time: O(n)
- Space:
  * Tabulation array: O(n)
  * Space-optimized: O(1)
"""

from typing import List


def climb(n: int) -> int:
    """Exact DP climb stairs from the reel."""
    if n <= 1:
        return 1
    dp = [1, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


def climb_optimized(n: int) -> int:
    """Space-optimized O(1) auxiliary space Fibonacci approach."""
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1


def climb_visual(n: int) -> int:
    print(f"\n{'='*55}")
    print(f"  FUN REEL 3: DYNAMIC PROGRAMMING (CLIMBING STAIRS)")
    print(f"{'='*55}")
    print(f"Calculating distinct ways for penguin to reach step {n}:\n")

    dp = [1, 1]
    print(f"Step 0: 1 way  (base)")
    print(f"Step 1: 1 way  (base)")

    for i in range(2, n + 1):
        val = dp[i - 1] + dp[i - 2]
        dp.append(val)
        print(f"Step {i}: dp[{i}] = dp[{i-1}] ({dp[i-1]}) + dp[{i-2}] ({dp[i-2]}) = {val}")

    print(f"\nResult: Exactly {dp[n]} distinct ways to climb {n} steps!")
    print(f"{'='*55}\n")
    return dp[n]


if __name__ == "__main__":
    climb_visual(6)
