1
"""
Interactive Algorithm Visualization Studio
12 Algorithm & Data Structure Demonstrations

Creator: Syeda Taqdees Bukhari
"""

import sys
import importlib

# Core Concepts
c1 = importlib.import_module("01_concepts.bubble_sort")
c2 = importlib.import_module("01_concepts.binary_search")
c3 = importlib.import_module("01_concepts.stack")
c4 = importlib.import_module("01_concepts.queue")
c5 = importlib.import_module("01_concepts.linked_list")
c6 = importlib.import_module("01_concepts.hanoi")
c7 = importlib.import_module("01_concepts.hash_table")

# Creative Animations
f1 = importlib.import_module("02_fun_animations.selection_sort")
f2 = importlib.import_module("02_fun_animations.bfs")
f3 = importlib.import_module("02_fun_animations.climbing_stairs")
f4 = importlib.import_module("02_fun_animations.tree_traversal")
f5 = importlib.import_module("02_fun_animations.two_pointers")

# ==========================================
# 2. INDIVIDUAL DEMONSTRATIONS
# ==========================================

def demo_1():
    c1.bubble_sort_visual([2, 1, 5, 3, 6, 7])


def demo_2():
    c2.binary_search_visual(
        [3, 8, 12, 17, 23, 29, 35, 42, 50], 42
    )


def demo_3():
    print("\nSTACK — LAST IN, FIRST OUT")

    stack = []
    for value in [10, 20, 30]:
        stack.append(value)
        print(f"Pushed: {value}")

    print("Stack:", stack)
    print("Popped:", stack.pop())
    print("Top item:", stack[-1])


def demo_4():
    print("\nQUEUE — FIRST IN, FIRST OUT")

    queue = deque()

    for value in ["A", "B", "C"]:
        queue.append(value)
        print(f"Enqueued: {value}")

    print("Queue:", list(queue))
    print("Dequeued:", queue.popleft())
    print("Remaining:", list(queue))


def demo_5():
    linked_list = c5.LinkedList()

    for value in [1, 2, 3]:
        linked_list.append(value)

    print("\nSINGLY LINKED LIST")
    linked_list.traverse()


def demo_6():
    print("\nTOWER OF HANOI")
    c6.hanoi(3, "A", "C", "B")


def demo_7():
    print("\nHASH TABLE — SEPARATE CHAINING")

    hash_table = c7.HashTable()

    for key in ["cat", "dog", "sun"]:
        hash_table.set(key, len(key))

    hash_table.display()


def demo_8():
    f1.selection_sort_visual([6, 4, 5, 3, 2, 1])


def demo_9():
    graph = {
        0: [1, 3, 4],
        1: [0, 4],
        3: [0, 6],
        4: [0, 1, 5],
        5: [4, 6],
        6: [3, 5]
    }

    f2.bfs_visual(graph, 0)


def demo_10():
    f3.climb_visual(6)


def demo_11():
    root = f4.TreeNode(
        4,
        f4.TreeNode(2, f4.TreeNode(1), f4.TreeNode(3)),
        f4.TreeNode(6, f4.TreeNode(5), f4.TreeNode(7))
    )

    print("\nBINARY TREE — IN-ORDER TRAVERSAL")
    print("Traversal:", f4.inorder(root))


def demo_12():
    f5.is_palindrome_visual("RACECAR")


# ==========================================
# 3. DEMO COLLECTION
# ==========================================

DEMOS = {
    "1": ("Bubble Sort", demo_1),
    "2": ("Binary Search", demo_2),
    "3": ("Stack — LIFO", demo_3),
    "4": ("Queue — FIFO", demo_4),
    "5": ("Singly Linked List", demo_5),
    "6": ("Tower of Hanoi", demo_6),
    "7": ("Hash Table", demo_7),
    "8": ("Selection Sort", demo_8),
    "9": ("Breadth-First Search", demo_9),
    "10": ("Dynamic Programming", demo_10),
    "11": ("Binary Tree Traversal", demo_11),
    "12": ("Two Pointers", demo_12)
}


def run_demo(choice):
    name, function = DEMOS[choice]

    print(f"\n{'=' * 55}")
    print(f"Starting: {name}")
    print(f"{'=' * 55}")

    try:
        function()
        print(f"\nCompleted: {name}")

    except Exception as error:
        print(f"\nError in {name}: {error}")


# ==========================================
# 4. RUN ALL DEMONSTRATIONS
# ==========================================

def run_all():
    print("\nRunning all 12 demonstrations...")

    for choice in DEMOS:
        run_demo(choice)

    print("\nAll demonstrations have finished!")


# ==========================================
# 5. MAIN MENU
# ==========================================

def menu():
    print("""
=============================================================
       ALGORITHM & DATA STRUCTURE VISUALIZATION STUDIO
                Creator: Syeda Taqdees Bukhari
=============================================================

  3D CODING CONCEPTS

  [1]  Bubble Sort
  [2]  Binary Search
  [3]  Stack — LIFO
  [4]  Queue — FIFO
  [5]  Singly Linked List
  [6]  Tower of Hanoi
  [7]  Hash Table

  FUN & CREATIVE ANIMATIONS

  [8]  Selection Sort — Penguin Animation
  [9]  Breadth-First Search — Spider Web Graph
  [10] Dynamic Programming — Climbing Stairs
  [11] Binary Tree — In-Order Traversal
  [12] Two Pointers — Palindrome Robot

  [A]  Run All Demonstrations
  [Q]  Quit

=============================================================
""")


# ==========================================
# 6. PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--all", "-a", "all"]:
        run_all()
        sys.exit(0)

    while True:
        menu()

        choice = input("Enter choice (1-12, A, Q): ").strip().upper()

        if choice == "Q":
            print("\nExiting. Happy coding!")
            break

        elif choice == "A":
            run_all()

        elif choice in DEMOS:
            run_demo(choice)

        else:
            print("\nInvalid selection. Please choose 1-12, A, or Q.")
