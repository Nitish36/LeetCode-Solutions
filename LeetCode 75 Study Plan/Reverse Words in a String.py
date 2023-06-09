class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        new_l = []

        for i in range(len(l)-1,-1,-1):
            new_l.append(l[i])
        
        new_s = ' '.join(new_l)
        return new_s
