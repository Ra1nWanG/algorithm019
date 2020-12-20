class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if not wordList or endWord not in wordSet:
            return 0
        left, right = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        count = 1
        while left:
            count += 1
            next_words = set()
            for word in left:
                for i in range(len(beginWord)):
                    for idx in range(26):
                        new = word[:i] + chr(97 + idx) + word[i + 1:]
                        if new in right:
                            return count
                        if new in wordSet and new not in visited:
                            next_words.add(new)
                            visited.add(new)
            left = next_words
            if len(left) > len(right):
                left, right = right, left
        return 0
