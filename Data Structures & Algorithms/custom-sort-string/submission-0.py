class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not s or len(s) == 1:
            return s
        countDict = defaultdict(int)
        redundant = ''
        for c in s:
            countDict[c] = countDict.get(c,0)+1
            if c not in order:
                redundant+=c
        res = ''
        for c in order:
            if c in countDict:
                res += c*countDict[c]
        return res+redundant

    