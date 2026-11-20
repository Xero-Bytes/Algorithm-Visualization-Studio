"""
Fun Reel 4: Binary Tree In-Order Traversal (Spider Tree)
Creator: Syeda Taqdees Bukhari

Description:
A recursive Depth-First Search traversal visiting nodes in the order:
1. Traverse Left Subtree
2. Visit & Process Current Node (Root)
3. Traverse Right Subtree
For a Binary Search Tree (BST), this visits nodes in non-decreasing order!

Complexity:
- Time: O(n) where n is the number of nodes
- Space: O(h) where h is the tree height (call stack)
"""

from typing import List, Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder(node: Optional[TreeNode], output: List[int] = None) -> List[int]:
    """Exact in-order traversal from the reel."""
    if output is None:
        output = []
    if node is None:
        return output
    inorder(node.left, output)
    output.append(node.val)
    inorder(node.right, output)
    return output


if __name__ == "__main__":
    print(f"\n{'='*55}")
    print(f"  FUN REEL 4: TREE TRAVERSAL (IN-ORDER)")
    print(f"{'='*55}")

    # Build the binary tree from the reel:
    #         4
    #       /   \
    #      2     6
    #     / \   / \
    #    1   3 5   7
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(6, TreeNode(5), TreeNode(7))

    print("Tree Structure:")
    print("        4       ")
    print("      /   \\    ")
    print("     2     6    ")
    print("    / \\  / \\   ")
    print("   1   3 5   7  \n")

    res = inorder(root)
    print(f"In-Order Traversal Order (Left -> Root -> Right):")
    print(f"  {' -> '.join(map(str, res))}")
    print(f"{'='*55}\n")
