class Solution:
    def twoSum(self,pairs: List[int], target: int)->List[int]:
        lptr=0
        rptr=len(pairs)-1
        result=list()
        while lptr<rptr:
            diff=target-pairs[lptr]
            if diff==pairs[rptr]:
                result.append([pairs[lptr],pairs[rptr]])
                lptr+=1
            elif diff<pairs[rptr]:
                rptr-=1
            else:
                lptr+=1
        return(result)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        finalresult=list()
        for i in range(len(nums)):
            trg=0-nums[i]
            res=self.twoSum(nums[i+1:],trg)
            for j in res:
                x=[nums[i]]
                x.extend(j)
                if x not in finalresult:
                    finalresult.append(x)
        return(finalresult)


        