class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = [""] * (len(word1) + len(word2))
        minimum = min(len(word1), len(word2))
        index1 = 0
        index2 = 0
        k = 0 

        
        for i in range(2 * minimum):
            if i % 2 == 0:
                word3[k] = word1[index1]
                index1 += 1
            else:
                word3[k] = word2[index2]
                index2 += 1
            k += 1 

        
        if index1 < len(word1):
            for i in range(index1, len(word1)):
                word3[k] = word1[index1]
                index1 += 1
                k += 1 
        
        if index2 < len(word2):
            for i in range(index2, len(word2)):
                word3[k] = word2[index2]
                index2 += 1
                k += 1 

        return "".join(word3)