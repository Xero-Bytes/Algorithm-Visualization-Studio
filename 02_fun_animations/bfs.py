"""
Fun Reel 2: Breadth-First Search (Spider Web Graph)
Creator: Syeda Taqdees Bukhari

Description:
Explores a graph level-by-level starting from a source node.
Uses a FIFO queue to guarantee that the shortest path (in terms
of number of edges) in an unweighted graph is discovered first.

Complexity:
- Time: O(V + E) where V = vertices, E = edges
- Space: O(V) for visited set and queue
"""

from collections import deque
from typing import Dict, List, Set


def bfs(g: Dict[int, List[int]], s: int) -> List[int]:
    """Exact Breadth-First Search from the reel."""
    seen: Set[int] = {s}
    q = deque([s])
    traversal: List[int] = []

    while q:
        u = q.popleft()
        traversal.append(u)
        for v in g.get(u, []):
            if v not in seen:
                seen.add(v)
                q.append(v)
    return traversal


def bfs_visual(g: Dict[int, List[int]], s: int) -> List[int]:
    """Detailed step-by-step BFS exploration trace."""
    seen: Set[int] = {s}
    q = deque([s])
    traversal: List[int] = []

    print(f"\n{'='*55}")
    print(f"  FUN REEL 2: BREADTH-FIRST SEARCH (SPIDER WEB)")
    print(f"{'='*55}")
    print(f"Start Node: {s}\n")

    step = 1
    while q:
        u = q.popleft()
        traversal.append(u)
        print(f"Step {step}: Visiting node {u} (Queue remaining: {list(q)})")
        for v in g.get(u, []):
            if v not in seen:
                seen.add(v)
                q.append(v)
                print(f"  -> Discovered neighbor {v} (added to queue)")
            else:
                print(f"  -> Neighbor {v} already seen")
        step += 1

    print(f"\nTraversal Order: {traversal}")
    print(f"{'='*55}\n")
    return traversal


if __name__ == "__main__":
    # Spider web graph from the reel
    graph = {
        0: [1, 3, 4],
        1: [0, 4],
        3: [0, 6],
        4: [0, 1, 5],
        5: [4, 6],
        6: [3, 5]
    }
    bfs_visual(graph, 0)
