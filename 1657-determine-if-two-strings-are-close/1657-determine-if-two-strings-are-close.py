class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1 = Counter(word1)
        map2 = Counter(word2)

        key1 = set(map1.keys())
        key2 = set(map2.keys())

        if key1 != key2:
            return False

        value1 = sorted(map1.values())
        value2 = sorted(map2.values())

        if value1 != value2:
            return False

        return True
