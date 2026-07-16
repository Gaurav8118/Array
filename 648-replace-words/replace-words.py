class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # Sort dictionary roots by length (shortest first)
        dictionary.sort(key=len)
        
        words = sentence.split()
        
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break   # stop at the shortest matching root
        
        return " ".join(words)
