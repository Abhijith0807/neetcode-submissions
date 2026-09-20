class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        patternMap = defaultdict(list)
        n = len(beginWord)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(n):
                pattern = word[:i]+"*"+word[i+1:]
                patternMap[pattern].append(word)
        q = deque([(beginWord,1)])
        visited = set([beginWord])
        while q:
            word,lvl = q.popleft()
            for i in range(n):
                pattern = word[:i]+"*"+word[i+1:]
                for word1 in patternMap[pattern]:
                    if word1 == endWord:
                        return(lvl+1)
                    if word1 not in visited:
                        visited.add(word1)
                        q.append((word1,lvl+1))
                del patternMap[pattern]
        return(0)