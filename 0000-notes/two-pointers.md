# Two Pointers

- Same direction
- Opposite direction

## Same Direction

> fast and slow pointers

0 --> i --> j --> n

[0,i): elements that have been processed

[i,j): elements that are not needed

[j,n): elements that have not been processed

## Opposite Direction

> left and right pointers

0 --> i --> <-- j <-- n

[0,i) and (j,n]: elements that have been processed

[i,j]: elements that are not processed

### Binary Search

### Two Sum

### Palindrome

Start from the middle and expand to both sides.

## Examples

- [LeetCode 344. Reverse String](../0344-Reverse-String/README.md)
- [LeetCode 26. Remove Duplicates from Sorted Array](../0026-Remove-Duplicates-From-Sorted-Array/README.md)
- [LeetCode 11. Container With Most Water](../0011-Container-With-Most-Water/README.md)
