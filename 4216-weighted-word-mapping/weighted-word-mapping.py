class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        r = []
        
        for w in words:
            s_w = 0
            
            for ch in w:
                s_w += weights[ord(ch) - ord('a')]
            
            value = s_w % 26
            
            r.append(chr(ord('z') - value))
        
        return "".join(r)