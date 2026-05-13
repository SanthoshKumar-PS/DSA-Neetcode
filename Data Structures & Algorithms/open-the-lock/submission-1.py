class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:])
                digit = str((int(lock[i])-1+10)%10)
                res.append(lock[:i]+digit+lock[i+1:])
            return res

        if '0000' in deadends:
            return -1
        
        queue = deque(['0000'])
        visited = set(deadends)
        visited.add('0000')
        count = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                lock = queue.popleft()
                if lock==target:
                    return count
                for child in children(lock):
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            count+=1

        return -1




