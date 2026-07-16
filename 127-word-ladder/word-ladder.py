class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 1
        queue = collections.deque()
        queue.append(beginWord)
        wordset = set(wordList)
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for x in "qwertyuiopasdfghjklzxcvbnm":
                        new_word = word[:i] + x + word[i+1:]
                        if new_word in wordset and new_word != word:
                            queue.append(new_word)
                            wordset.remove(new_word)

            res += 1

        return 0