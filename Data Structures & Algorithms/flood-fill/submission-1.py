class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        starting = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if r<0 or r==len(image) or c<0 or c==len(image[0]) or image[r][c]!=starting:
                    continue
                queue.append((r,c))
                image[r][c] = color
        return image
