"""
Fun Reel 5: Two Pointers (Robot Palindrome Check)
Creator: Syeda Taqdees Bukhari

Description:
Two robots (left 'l' and right 'r' pointers) start at opposite ends
of a string and march towards the center, comparing characters.
If all symmetric character pairs match, the string is a palindrome.

Complexity:
- Time: O(n) (Traverses each character at most once)
- Space: O(1) auxiliary (In-place pointer comparison)
"""


def is_palindrome(s: str) -> bool:
    """Exact two pointers palindrome checker from the reel."""
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def is_palindrome_visual(s: str) -> bool:
    """Detailed visual trace of the two robot pointers."""
    l, r = 0, len(s) - 1
    step = 1

    print(f"\n{'='*55}")
    print(f"  FUN REEL 5: TWO POINTERS (ROBOT PALINDROME)")
    print(f"{'='*55}")
    print(f"Input Word: \"{s}\"\n")

    while l < r:
        char_l, char_r = s[l], s[r]
        pointer_line = [" "] * len(s)
        pointer_line[l] = "L"
        pointer_line[r] = "R"
        p_str = "".join(pointer_line)

        print(f"Step {step}:")
        print(f"  Word:     {' '.join(s)}")
        print(f"  Pointers: {' '.join(p_str)}")
        print(f"  Left robot arr[{l}]='{char_l}' == Right robot arr[{r}]='{char_r}' ? {'YES' if char_l == char_r else 'NO'}")

        if char_l != char_r:
            print(f"  -> Mismatch found! '{s}' is NOT a palindrome.\n")
            return False
        l += 1
        r -= 1
        step += 1

    print(f"  -> All pairs matched! \"{s}\" is a valid palindrome! \u2714\n")
    print(f"{'='*55}\n")
    return True


if __name__ == "__main__":
    is_palindrome_visual("RACECAR")
    is_palindrome_visual("ALGORITHM")
