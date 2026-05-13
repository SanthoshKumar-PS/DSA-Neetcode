class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsList = set(wordList)
        if endWord not in wordsList:
            return 0
        queue = deque([[beginWord, 1]])
        if beginWord in wordsList:
            wordsList.remove(beginWord)

        while queue:
            word, count = queue.popleft()
            if word==endWord:
                return count
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordsList:
                        queue.append([newWord,count+1])
                        wordsList.remove(newWord)
        return 0