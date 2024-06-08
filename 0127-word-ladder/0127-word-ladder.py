class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        q = deque()
        wordList = set(wordList)
        q.append((beginWord, 1))

        while q:
            word, step = q.popleft()
            for i in range(len(beginWord)):
                for j in range(26):
                    new_word = word[:i] + chr(97 + j) + word[i + 1:]
                    if new_word == endWord:
                        return step + 1
                    if new_word in wordList:
                        q.append((new_word, step + 1))
                        wordList.remove(new_word)
        
        return 0

