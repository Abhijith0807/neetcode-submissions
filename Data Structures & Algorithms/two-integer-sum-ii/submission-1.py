class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr,rptr=0,len(numbers)-1
        while lptr<rptr:
            summ=numbers[lptr]+numbers[rptr]
            if summ==target:
                return([lptr+1,rptr+1])
            elif summ>target:
                rptr-=1
            else:
                lptr+=1