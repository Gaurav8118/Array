class Solution:
    def findRelativeRanks(self, score):
        # Sort scores in descending order with their original indices
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        
        # Prepare result array
        result = [""] * len(score)
        
        # Assign ranks
        for rank, (idx, _) in enumerate(sorted_scores, start=1):
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)
        
        return result

