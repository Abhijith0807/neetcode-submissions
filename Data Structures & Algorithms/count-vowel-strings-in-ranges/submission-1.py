class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','i','o','u']
        res = []
        for i,j in queries:
            out = 0 
            for s in words[i:j+1]:
                if s[0] in vowels and s[-1] in vowels:
                    out+=1
            res.append(out)
        return res