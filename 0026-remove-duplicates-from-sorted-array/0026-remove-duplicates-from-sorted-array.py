class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            if i == 0 or nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1

            j +=1
        
        return i