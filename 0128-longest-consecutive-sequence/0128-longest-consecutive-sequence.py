class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = defaultdict(list)
        max_len = 0
        for n in nums:
            if m.get(n):
                continue
            l, r = n, n
            if m[n + 1]:
                r = m[n + 1][1]
            if m[n - 1]:
                l = m[n - 1][0]
            m[l] = m[r] = m[n] = [l, r]
            max_len = max(max_len, r - l + 1)

        return max_len