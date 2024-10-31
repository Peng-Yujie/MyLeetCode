class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        i = 0

        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1
            
            chars[res] = ch
            res += 1

            if count > 1:
                for digit in str(count):
                    chars[res] = digit
                    res += 1
            
        return res