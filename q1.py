"""
Q1: Stable Character

You are given a string `s`.

In this string, some characters may appear multiple times.

A character is called **stable** if all of its occurrences appear **together as
one continuous group**, without being interrupted by other characters.

Your task is to identify the **first stable character** you encounter when
reading the string from left to right.

If the string does not contain any stable character, return `None`.

Examples:
---------
Input: "aaabccddde"  → Output: 'a'
Input: "abccba"      → Output: 'c'
Input: "aabbcc"      → Output: 'a'
Input: "abc"         → Output: None
Input: "a"           → Output: None

Explanation:
- In "abccba", 'c' appears at positions 2,3 (continuous), while 'a' and 'b'
  are interrupted
- Single character occurrences are not considered stable (must appear at least
  twice)
"""

def first_stable_character(s):

    if not s:
        return None

    first_pos = {}
    last_pos = {}
    
    for i, char in enumerate(s):
        if char not in first_pos:
            first_pos[char] = i
        last_pos[char] = i

    for i, char in enumerate(s):
                if (
            first_pos[char] != last_pos[char] and
            first_pos[char] == i and
            s[first_pos[char]: last_pos[char] + 1] == char * (last_pos[char] - first_pos[char] + 1)
        ):
                     return char
                     
    return None

if __name__ == "__main__":
    # Test your solution here
    print(first_stable_character("abccba"))  # Should print: c
    print(first_stable_character("abc"))     # Should print: None
    print(first_stable_character("a"))       # Should print: None
