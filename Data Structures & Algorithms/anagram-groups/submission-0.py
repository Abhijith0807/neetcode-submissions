class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            count_alpha=[0]*26
            for c in s:
                count_alpha[ord(c)-ord('a')]+=1
            hashmap[tuple(count_alpha)].append(s)
        return(hashmap.values())