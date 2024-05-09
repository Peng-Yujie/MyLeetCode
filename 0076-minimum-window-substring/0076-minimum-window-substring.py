class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        window = {}

        for ch in t:
            window[ch] = 1 + window.get(ch, 0)
        
        left, count, start, min_len = 0, 0, 0, float("infinity")

        for right in range(len(s)):
            ch = s[right]

            if window.get(ch, 0) > 0:
                count += 1
            
            window[ch] = window.get(ch, 0) - 1

            if count == len(t):
                ch2 = s[left]

                while left < right and window.get(ch2, 0) < 0:
                    window[ch2] = 1 + window.get(ch2, 0)
                    left += 1
                    ch2 = s[left]
                
                if min_len > (right - left):
                    min_len = right -left + 1
                    start = left
                
                window[ch2] = 1 + window.get(ch2, 0)
                left += 1
                count -= 1
        
        return s[start:start+min_len] if min_len <= len(s) else ""
