class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        start, max_len = 0, 0
        
        for end in range(len(s)):
            ch = s[end]
            window[ch] = 1 + window.get(ch, 0)
            while window[ch] > 1:
                ch2 = s[start]
                window[ch2] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)
        
        return max_len
