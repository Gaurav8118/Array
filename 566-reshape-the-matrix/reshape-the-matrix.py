class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
        
        # Flatten the matrix
        flat = [num for row in mat for num in row]
        
        # Build reshaped matrix
        result = []
        for i in range(r):
            result.append(flat[i*c:(i+1)*c])
        
        return result
