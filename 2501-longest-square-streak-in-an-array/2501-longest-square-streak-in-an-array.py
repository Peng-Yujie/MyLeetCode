class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        seen = {}
        ans = -1

        for n in nums:
            if n * n in seen:
                seen[n] = seen[n * n] + 1
                ans = max(ans, seen[n])
            else:
                seen[n] = 1

        return ans
