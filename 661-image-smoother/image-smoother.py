class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        # Directions for 8 neighbors + itself
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),  (0,0),  (0,1),
                      (1,-1),  (1,0),  (1,1)]
        
        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        total += img[x][y]
                        count += 1
                result[i][j] = total // count   # floor division
        
        return result
