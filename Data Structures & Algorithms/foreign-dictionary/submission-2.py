class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        queue = deque()
        graph = defaultdict(list)
        indegree = {char:0 for word in words for char in word}
        result = []
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            if len(word1)>len(word2) and word1.startswith(word2):
                return ""
            for j in range(len(word1)):
                if word1[j]==word2[j]:
                    continue
                indegree[word2[j]]+=1
                graph[word1[j]].append(word2[j])
                break
        for char, degree in indegree.items():
            if degree==0:
                queue.append(char)
        print(queue)
        print(graph)
        print(indegree)
        while queue:
            char = queue.popleft()
            result.append(char)
            for neigh in graph[char]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)

        return "".join(result) if len(result)==len(indegree) else ""
