class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        queue = deque()
        graph = defaultdict(list)
        indegree = {char:0 for word in words for char in word}
        result = []
        for j in range(n-1):
            word1, word2 = words[j], words[j+1]
            if len(word1)>len(word2) and word1.startswith(word2):
                return ""
            for i in range(min(len(word1),len(word2))):
                if word1[i]==word2[i]:
                    continue
                graph[word1[i]].append(word2[i])
                indegree[word2[i]]+=1
                break
        for char, deg in indegree.items():
            if deg==0:
                queue.append(char)
        
        while queue:
            char = queue.popleft()
            result.append(char)
            for neigh in graph[char]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        
        if(len(result)!=len(indegree)):
            return ""

        return "".join(result)