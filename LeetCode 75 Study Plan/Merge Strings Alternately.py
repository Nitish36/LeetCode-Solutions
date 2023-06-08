class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = [i for i in word1]
        l2 = [j for j in word2]
        l3 = []
        s3 = ""
        i = 0
        j = 0
        while i<len(l1) or j<len(l2):
            if i<len(l1):
                l3.append(l1[i])
                i = i+1
            if j<len(l2):
                l3.append(l2[j])
                j = j+ 1
        
        s3 = ''.join(l3)
        return s3
