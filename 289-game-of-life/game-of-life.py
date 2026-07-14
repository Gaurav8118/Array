class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        
        def countLiveNeighbors(r, c):
            count = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >= m or j >= n:
                        continue
                    count += board[i][j] & 1  # only current state
            return count
        
        # Step 1: Compute next state and store in 2nd bit
        for r in range(m):
            for c in range(n):
                live_neighbors = countLiveNeighbors(r, c)
                
                # Rule application
                if board[r][c] & 1:  # currently live
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[r][c] |= 2  # set next state to live
                else:  # currently dead
                    if live_neighbors == 3:
                        board[r][c] |= 2  # set next state to live
        
        # Step 2: Update board to next state
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1
