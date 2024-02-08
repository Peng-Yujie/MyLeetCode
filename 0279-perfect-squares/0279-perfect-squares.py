class Solution:
    def numSquares(self, n: int) -> int:
        def fn(i, target, current_len, min_len):
            if target == 0:
                return min(current_len, min_len)
            
            if i < 1 or current_len >= min_len:
                return min_len
            
            if i**2 <= target:
                min_len = fn(i, target - i**2, current_len + 1, min_len)
            
            min_len = fn(i-1, target, current_len, min_len)
            return min_len
        
        return fn(int(math.sqrt(n)), n, 0, n)

        # def fn(i, target):
        #     if target < 0:
        #         return n

        #     if target == 0:
        #         return 0
            
        #     if i == 1:
        #         return target
            
        #     take_current = 1 + fn(i, target - i**2)
            
        #     skip_current = fn(i - 1, target)
            
        #     return min(take_current, skip_current)
        
        # return fn(int(math.sqrt(n)), n)