class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)
        if not wordList or not endWord in wordSet:
            return 0
        visited = {beginWord, endWord}
        left, right = {beginWord}, {endWord}
        count = 0
        while left:
            count += 1
            next_words = set()
            for word in left:
                for i in range(len(beginWord)):
                    for idx in range(26):
                        new_word = word[:i] + chr(97 + idx) + word[i + 1:]
                        if new_word in right:
                            return count + 1
                        if new_word not in visited and new_word in wordSet:
                            visited.add(new_word)
                            next_words.add(new_word)
            left = next_words
            if len(left) > len(right):
                left, right = right, left
        return 0
