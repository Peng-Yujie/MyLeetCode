# Binary Search

- sorted array
- O(log n) time complexity
- shrink the search space every iteration
- DO NOT exclude potential answers in the search space

## Templates

1. Find a accurate value
2. Find a fuzzy value
3. Common use cases

```
1, 1, 2, 2, 2, 6, 7
```

### Find 1st occurrence of a value (fuzzy)

- loop condition: `l < r`
- shrink search space:
    - `r = mid`, `l = mid + 1`

### Find last occurrence of a value (fuzzy)

- loop condition: `l < r`
- shrink search space:
    - `l = mid`, `r = mid - 1`

### Find the value closest to a target

- loop condition: `l < r - 1`
- shrink search space:
    - `mid = l + (r - l) / 2`
    - `if nums[mid] < target: l = mid`
    - `if nums[mid] > target: r = mid`

## Examples

### LeetCode 1062. Longest Repeating Substring

Given a string `s`, find out the length of the longest repeating substring. Return 0 if no repeating substring exists.

Example 1:

```python
Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
```

Example 2:

```python
Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
```

#### Solution

Force brute: O(n^3)

Binary search: O(n^2 * log n)

```python
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if self.search(S, mid):
                l = mid
            else:
                r = mid - 1
        return l

    def search(self, S, length):
        seen = set()
        for i in range(len(S) - length + 1):
            if S[i:i + length] in seen:
                return True
            seen.add(S[i:i + length])
        return False
```
