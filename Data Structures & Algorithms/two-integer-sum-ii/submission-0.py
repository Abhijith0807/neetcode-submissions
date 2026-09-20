class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rptr=len(numbers)-1
        for lptr in range(len(numbers)):
            diff=target-numbers[lptr]
            while diff<numbers[rptr]:
                rptr=rptr-1
            if diff==numbers[rptr]:
                return([lptr+1,rptr+1])
            
        