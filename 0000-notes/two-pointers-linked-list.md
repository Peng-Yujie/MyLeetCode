# Solve linked list problems with two pointers

[Two Pointers](two-pointers.md) is a technique that is often used to solve linked list problems. The two pointers can be in the same direction or in opposite directions.

## LeetCode 21. Merge Two Sorted Lists

[LeetCode 21. Merge Two Sorted Lists](../0021-merge-two-sorted-lists/)

**Solution:**

- Create a dummy node.
- Use two pointers to traverse the two lists.
- Compare the values of the two pointers.
- Append the smaller value to the dummy node.
- Move the pointer of the smaller value first.
- Continue until one of the pointers reaches the end.
- Append the remaining nodes to the dummy node.
- Return the next node of the dummy node.

**More:**

- [LeetCode 23. Merge k Sorted Lists](../0023-merge-k-sorted-lists/)
  - Priority Queue (Heap queue)
  - **Note:**
    - In Python3, the cmp() special method is removed.
    - Store entries as tuples (priority, entry_index, node), where entry_index is used to break ties by comparing nodes.

## LeetCode 86. Partition List

[LeetCode 86. Partition List](../0086-partition-list/)

**Solution:**

- Create two dummy nodes. (For two partitions in the result)
- Create a pointer for traversing the original list.
- Use two pointers to append nodes to the two partitions.
- Connect the two partitions.
- Return the next node of the first dummy node.
